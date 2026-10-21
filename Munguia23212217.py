"""
Práctica 2: Sistema Cardiovascular

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Yesenia Isamar Munguia Silva
Número de control: 23212217
Correo institucional: l23212217@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx


"""

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import pandas as pd
import scipy.signal as signal_scipy


# Datos simulación

u_excel = np.array(pd.read_excel('signal.xlsx', header=None))
u = np.reshape(u_excel,-1)
x0, t0, tend, dt, w, h = 0, 0, 15, 1E-3, 10, 5
N_steps = round(tend/dt) + 1
t = np.linspace(t0, tend, N_steps)
u = np.reshape(signal_scipy.resample(u_excel, len(t)),-1).real

signals = ['Presión']


# Función corazón

def heart(R, L, C, Z):
    num = [L*R, R*Z]
    den = [C*L*R*Z, L*(Z + R), R*Z]
    sys = ctrl.tf(num, den)
    print(f"Funcion de transferencia cardiovascular:\n{sys}\n")
    return sys


# Función controlador PID

def controlador(kP, kI, kD, sys):
    Cr = 1E-6
    Re = 1/(Cr*kI)
    Rr = kP*Re
    Ce = kD/Rr
    numPID = [Re*Rr*Ce*Cr,Re*Ce + Rr*Cr,1]
    denPID = [Re*Cr, 0]
    PID = ctrl.tf(numPID, denPID)
    print(f"Capacitancia Cr: {Cr} F")
    print(f"Resistencia Re: {Re} Ohms")
    print(f"Resistencia Rr: {Rr} Ohms")
    print(f"Capacitancia Ce: {Ce} F")
    print(f"Funcion de transferencia PID:\n{PID}\n")
    sysPID = ctrl.feedback(ctrl.series(PID, sys),1,sign=-1)
    print(f"Sistema en lazo cerrado:\n{sysPID}\n")

    return sysPID


# Parámetros de Normotenso, Hipotenso e Hipertenso

Z, R, L = 0.010, 1.000, 0.001

C_normo = 1.500
C_hipo = 3.500
C_hiper = 1.000


# Sistemas de lazo abierto

sys_normo = heart(R, L, C_normo, Z)
sys_hipo = heart(R, L, C_hipo, Z)
sys_hiper = heart(R, L, C_hiper, Z)


# Parámetros de los controladores **los del 6 de Octubre

P_hipo, I_hipo, D_hipo = 62.299, 143640.9879, 0.00082872
P_hiper, I_hiper, D_hiper = 1611.193, 3845842.36679, 0.0226422


# Crear sistemas controlados en lazo cerrado

sysPID_hipo = controlador(P_hipo, I_hipo, D_hipo, sys_hipo)
sysPID_hiper = controlador(P_hiper, I_hiper, D_hiper, sys_hiper)


# Funciones del sistema en lazo abierto y lazo cerrado

def openloop(t, sys, u_signal):
    _, y = ctrl.forced_response(
        sys, T=t, U=u_signal, X0=x0
    )
    return np.asarray(y).flatten()


def closedloop(t, sysPID, u_signal):
    _, y = ctrl.forced_response(
        sysPID, T=t, U=u_signal, X0=x0
    )
    return np.asarray(y).flatten()


y_normo = openloop(t, sys_normo, u)
y_hipo = openloop(t, sys_hipo, u)
y_hiper = openloop(t, sys_hiper, u)

y_PID_hipo = closedloop(t, sysPID_hipo, u)
y_PID_hiper = closedloop(t, sysPID_hiper, u)


# Gráficas

plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

clr1 = np.array([149,100,221])/255
clr2 = np.array([255,190,145])/255
clr3 = np.array([118,196,87])/255


# Normotenso

fg1 = plt.figure(1)
fg1.set_size_inches(w, h)

plt.plot(t, y_normo, '-', color=clr1, label='$P_{p}(t)$: Normotenso')
plt.plot(t, y_hipo, '--', color=clr2, label='$P_{p}(t)$: Hipotenso')
plt.plot(t, y_hiper, ':', color=clr3, label='$P_{p}(t)$: Hipertenso')

plt.xlim(0, 15)
plt.xticks(np.arange(0, 16, 1))
plt.ylim(-0.4, 1.2)
plt.yticks(np.arange(-0.4, 1.4, 0.2))

plt.xlabel('t [s]')
plt.ylabel('Respuesta [V]')

plt.legend(loc='lower center',bbox_to_anchor=(0.5, 1.02),ncol=3,frameon=False)

fg1.savefig(f"{signals[0]}_Normotenso.pdf",bbox_inches='tight')
plt.show()


# Control Hipotenso

fg2 = plt.figure(2)
fg2.set_size_inches(w, h)

plt.plot(t, y_normo, '-', color=clr1, label='$P_{p}(t)$: Normotenso')
plt.plot(t, y_hipo, '--', color=clr2, label='$P_{p}(t)$: Hipotenso')
plt.plot(t, y_PID_hipo, ':',linewidth=2.5, color=clr3, label='$PID(t)$: Hipotenso')

plt.xlim(0, 15)
plt.xticks(np.arange(0, 16, 1))
plt.ylim(-0.4, 1.2)
plt.yticks(np.arange(-0.4, 1.4, 0.2))

plt.xlabel('t [s]')
plt.ylabel('Respuesta [V]')

plt.legend(loc='lower center',bbox_to_anchor=(0.5, 1.02),ncol=3,frameon=False)

fg2.savefig(f"{signals[0]}_Control_Hipotenso.pdf",bbox_inches='tight')

plt.show()


# Control Hipertenso

fg3 = plt.figure(3)
fg3.set_size_inches(w, h)

plt.plot(t, y_normo, '-', color=clr1, label='$P_{p}(t)$: Normotenso')
plt.plot(t, y_hiper, '--', color=clr2, label='$P_{p}(t)$: Hipertenso')
plt.plot(t, y_PID_hiper, ':',linewidth=2.5, color=clr3, label='$PID(t)$: Hipertenso')

plt.xlim(0, 15)
plt.xticks(np.arange(0, 16, 1))
plt.ylim(-0.4, 1.2)
plt.yticks(np.arange(-0.4, 1.4, 0.2))

plt.xlabel('t [s]')
plt.ylabel('Respuesta [V]')

plt.legend(loc='lower center',bbox_to_anchor=(0.5, 1.02),ncol=3,frameon=False)

fg3.savefig(f"{signals[0]}_Control_Hipertenso.pdf",bbox_inches='tight')

plt.show()