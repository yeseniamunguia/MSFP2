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

En esta práctica se estudia el modelo Windkessel de cuatro elementos, que representa de forma simplificada la dinámica del sistema arterial mediante un circuito eléctrico equivalente. La presión sanguínea se relaciona con el voltaje y el flujo sanguíneo con la corriente. El elemento Z representa la impedancia característica de la región proximal del sistema arterial; R corresponde a la resistencia periférica que se opone al flujo; C representa la distensibilidad arterial, es decir, la capacidad de los vasos para almacenar volumen al aumentar la presión; y L representa la inertancia asociada con la aceleración y desaceleración de la sangre. Estas correspondencias permiten relacionar el comportamiento del circuito con las propiedades mecánicas de la circulación arterial.

En el circuito, Z y L están conectados en paralelo entre el nodo de presión de entrada Pa(t) y el nodo de presión de salida Pp(t), mientras que C y R están conectados en paralelo entre la salida y el nodo de referencia. El flujo de entrada se divide entre Z y L y posteriormente se distribuye entre C y R. Aunque el modelo contiene cuatro elementos, su dinámica es de segundo orden porque únicamente la capacitancia y la inductancia almacenan energía de manera independiente. El análisis matemático comprende la obtención de la función de transferencia del circuito entre la presión de salida y la presión de entrada, el estudio de la estabilidad en lazo abierto para los casos normotenso, hipertenso e hipotenso, el cálculo del error en estado estacionario y la formulación del modelo de ecuaciones integrodiferenciales mediante las relaciones de los componentes y las leyes de Kirchhoff. El modelo de ecuaciones diferenciales ordinarias (EDOs) se trabaja exclusivamente en el cuaderno computacional de MATLAB, utilizando como variables de estado el flujo a través de L y la presión sobre C.

Se consideran tres conjuntos de parámetros correspondientes a los individuos normotenso, hipertenso e hipotenso. En todos ellos se mantienen Z en 0.010 mmHg·s/ml, L en 0.001 mmHg·s²/ml y R en 1.000 mmHg·s/ml. La distensibilidad C toma los valores de 1.500 ml/mmHg para el normotenso, 1.000 ml/mmHg para el hipertenso y 3.500 ml/mmHg para el hipotenso. Dentro de esta representación, el caso hipertenso tiene menor capacidad de distensión, mientras que el hipotenso tiene mayor capacidad para almacenar volumen ante una variación de presión. Estas modificaciones afectan la respuesta dinámica de los modelos y permiten analizar sus diferencias respecto al individuo normotenso.

Para las simulaciones se genera una señal aleatoria mediante el bloque Uniform Random Number de Simulink, con mínimo de −0.2, máximo de 1, semilla de 106 y tiempo de muestreo de 0.1 s, durante un intervalo de 0 a 15 s. Esta señal se aplica al modelo normotenso y la salida obtenida se utiliza como entrada de los modelos hipertenso e hipotenso sin controlador. De esta manera, cada caso se conecta en cascada con el modelo normotenso, por lo que sus respuestas dependen tanto de sus propios parámetros como de la señal previamente procesada por dicho modelo. El archivo signal forma parte de los archivos utilizados en la práctica para trabajar con las señales de simulación.

El control se realiza mediante dos lazos de retroalimentación independientes, uno para el caso hipertenso y otro para el hipotenso. En ambos se toma la salida normotensa como referencia y se compara con la salida del caso controlado para obtener la señal de error. El PID procesa este error y genera la entrada aplicada al modelo correspondiente. Sus acciones proporcional, integral y derivativa responden, respectivamente, al error presente, a su acumulación y a su variación, con el propósito de mejorar el seguimiento de la referencia. Las ganancias se sintonizan por separado para cada caso y se conservan las imágenes de sus parámetros. Así, en las simulaciones sin controlador la salida normotensa alimenta directamente a cada caso, mientras que en los lazos cerrados funciona como referencia y la entrada de cada caso es producida por su PID.

El cuaderno computacional de MATLAB incluye las funciones de transferencia y el modelo mediante EDOs, lo que permite comparar ambas representaciones del sistema. En Python se implementan las funciones de transferencia y los sistemas con los controladores correspondientes. Se generan tres gráficas en Python, denominadas Individuos, Hipertenso e Hipotenso, y cuatro en MATLAB, denominadas Individuos, Individuos EDOs, Hipertenso e Hipotenso. Las gráficas de individuos muestran las señales normotensa, hipertensa e hipotensa sin controlador; la gráfica Individuos EDOs presenta estas respuestas obtenidas mediante las ecuaciones diferenciales. En la gráfica Hipertenso se comparan la señal normotensa, la hipertensa sin controlador y la hipertensa con PID; en la gráfica Hipotenso se realiza la comparación equivalente. Estas representaciones permiten evaluar el comportamiento transitorio, las diferencias respecto a la referencia y el efecto de los controladores, además de comparar las implementaciones de MATLAB y Python. El diagrama elaborado en BioRender complementa el análisis al relacionar los elementos eléctricos con las estructuras y propiedades cardiovasculares que representan.

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
