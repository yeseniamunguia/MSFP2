[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=yeseniamunguia/MSFP2)

# Práctica: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información de la estudiante

Yesenia Isamar Munguia Silva [23212217]; l23212217@tijuana.tecnm.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Identificar las variables y los parámetros del modelo Windkessel de cuatro elementos y relacionarlos con las propiedades hemodinámicas que representan.
2. Determinar el modelo de ecuaciones integrodiferenciales del circuito.
3. Obtener las funciones de transferencia de los modelos normotenso, hipertenso e hipotenso.
4. Analizar la estabilidad en lazo abierto de cada caso mediante la localización de sus polos y determinar el error en estado estacionario.
5. Implementar los modelos matemáticos en MATLAB/Simulink e incluir las funciones de transferencia y el modelo de EDOs en el cuaderno computacional de MATLAB.
6. Simular la respuesta del modelo normotenso a una señal aleatoria y utilizar su salida como entrada de los modelos hipertenso e hipotenso sin controlador para comparar las respuestas de los tres individuos.
7. Diseñar y sintonizar dos controladores PID independientes para reducir las diferencias de los casos hipertenso e hipotenso respecto a la respuesta normotensa.
8. Comparar, para cada caso, la respuesta normotensa, la respuesta sin controlador y la respuesta con PID, considerando el seguimiento de la referencia, el error y el comportamiento transitorio.
9. Implementar las funciones de transferencia y los sistemas controlados en Python mediante Visual Studio Code y comparar sus resultados con los obtenidos en MATLAB, incluyendo la comparación entre funciones de transferencia y EDOs en el cuaderno computacional.
10. Elaborar un diagrama en BioRender que relacione los componentes del modelo con las estructuras cardiovasculares y documentar los análisis, las simulaciones y los parámetros de los controladores en el repositorio.

## Descripción detallada del sistema

En esta práctica se estudia el modelo Windkessel de cuatro elementos, que representa la dinámica del sistema arterial mediante un circuito eléctrico equivalente. La presión sanguínea se relaciona con el voltaje y el flujo con la corriente. Sus componentes son Z, que representa la impedancia característica; R, la resistencia periférica; C, la distensibilidad arterial; y L, la inertancia sanguínea. El modelo presenta una dinámica de segundo orden debido a sus dos elementos almacenadores de energía: C y L.

Se analizan los casos normotenso, hipertenso e hipotenso mediante la función de transferencia, la estabilidad en lazo abierto, el error en estado estacionario y las ecuaciones integrodiferenciales. Los parámetros Z, L y R se mantienen constantes, mientras que C toma valores de 1.500, 1.000 y 3.500 ml/mmHg, respectivamente, lo que permite estudiar cómo la distensibilidad modifica la respuesta del sistema.

Las simulaciones se realizan con una señal aleatoria generada en Simulink durante 15 segundos. La salida normotensa se utiliza como entrada de los modelos hipertenso e hipotenso sin controlador y como referencia para sus respectivos lazos de control PID. Estos controladores buscan mejorar el seguimiento de la referencia mediante acciones proporcional, integral y derivativa.

Finalmente, se implementan las funciones de transferencia en Python y MATLAB, mientras que el modelo mediante ecuaciones diferenciales ordinarias se desarrolla exclusivamente en MATLAB. Se generan gráficas para comparar las respuestas de los tres individuos, las implementaciones mediante EDOs y el efecto de los controladores PID. Además, un diagrama en BioRender ilustra la relación entre los componentes del circuito y las propiedades cardiovasculares que representan.

Palabras clave: Modelo Windkessel; Sistema cardiovascular; Controlador PID; Modelo matemático; Simulaciones numéricas.

## Lista de archivos incluidos en el repositorio

1. Diagrama biológico elaborado en BioRender.
2. Cuaderno computacional de MATLAB [.mlx y .pdf].
3. Imágenes con los parámetros de los controladores hipertenso e hipotenso.
4. Análisis matemático: función de transferencia del circuito, estabilidad en lazo abierto de cada caso, error en estado estacionario y modelo de ecuaciones integrodiferenciales.
5. Archivo signal.
6. Código de Python [.py].
7. Imágenes de las simulaciones en Python (3): Individuos, Hipertenso e Hipotenso.
8. Imágenes de las simulaciones en MATLAB (4): Individuos, Individuos EDOs, Hipertenso e Hipotenso.

## Referencias

[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Sección 5.4, “Práctica: Modelado y control del sistema cardiovascular mediante el modelo Windkessel”, pp. 76–86.

[2] M. C. Khoo, Physiological Control Systems: Analysis, Simulation, and Estimation, 2nd ed. IEEE Press, 2018.

[3] N. S. Nise, Control Systems Engineering, 8th ed. John Wiley & Sons, 2020.
