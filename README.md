# ia-para-juegos
Repositorio de ia para el electivo "inteligencia artificial para videojuegos"

Proyecto originalmente hecho en python 2.X 
Traducción a python3 sacada del siguiente repositorio: https://github.com/jspacco/pac3man/tree/master/multiagent

Explicación de la logica de códigos para tarea 1. (Esto es solo para ayudarme a aprender, escribo todo lo que voy viendo y asi no se me olvidan detalles importantes)

Question 1.
Mejoré la función de evaluación para crear un equilibrio entre la búsqueda activa de comida y la evasión  de los fantasmas. Utilizo la distancia de Manhattan, una medida simple y eficiente, para evaluar qué tan cerca está Pacman de la comida y los fantasmas asustados, otorgando recompensas basadas en esta proximidad. Para evitar que Pacman caiga en patrones repetitivos de huida (como estar dando vueltas sin sentido), he introducido una penalización significativa si un fantasma no asustado se encuentra demasiado cerca.  

Question 2.
Max Value()
Representa la lógica de decisión de Pacman. Se busca el valor máximo entre los valores devueltos por minValue, representando el mejor resultado posible para Pacman tras los movimientos de los fantasmas.

Min Value()
Representa la lógica de decisión de los fantasmas. Itera sobre las acciones legales del fantasma y llama a maxValue o minValue según corresponda, buscando el valor más bajo para simular la mejor jugada de los fantasmas.

getAction()
Función principal que determina la acción de Pacman. Itera sobre las acciones legales de Pacman y llama a minValue para el primer fantasma. La acción que conduce al valor más alto es seleccionada, asumiendo que los fantasmas juegan de manera óptima

Question 4 y 5 (Tuve que hacer la 4 para poder hacer la 5)

getAction() utiliza una función lambda para elegir la acción que maximiza el valor esperado, calculado por getActionValue. Lambda es eficiente para pasar funciones simples directamente dentro de llamadas a otras funciones, en este caso, seleccionando la acción óptima sin necesidad de una declaración de función adicional.

getActionValue() asigna valores a las acciones de Pacman y fantasmas. Para Pacman, maxValue busca la acción con la mayor evaluación positiva. Para los fantasmas, expectValue calcula un promedio de valores posibles, reflejando su comportamiento aleatorio. Este promedio es el "valor esperado", que es crucial para la estrategia de Pacman, ya que permite anticipar y planificar contra movimientos aleatorios de los fantasmas.

expectValue() primero verifica si el juego ha terminado o si se ha alcanzado la profundidad de búsqueda deseada. Si es así, devuelve la evaluación del estado actual. Si no, evalúa todas las acciones legales del fantasma, generando estados sucesores y obteniendo sus valores mediante llamadas recursivas. El valor esperado se obtiene promediando estos valores, proporcionando una estimación ponderada de los posibles resultados dados los movimientos aleatorios del fantasma.

betterEvaluationFunction() es una fórmula que Pacman usa para decidir qué tan bueno es un movimiento. Esta fórmula mira varias cosas importantes: qué tan cerca está la comida más próxima, cuánta comida queda por comer, si hay fantasmas cerca que Pacman puede comer porque están asustados, y si hay fantasmas peligrosos cerca que pueden comer a Pacman. También toma en cuenta cuántas cápsulas especiales quedan, que hacen a los fantasmas asustarse, y cuántos puntos tiene Pacman en ese momento. La idea es que Pacman prefiera los movimientos que lo acerquen a la comida y a los fantasmas asustados, y que evite los fantasmas peligrosos y ahorre las cápsulas especiales. Todo esto se combina para darle a Pacman una puntuación para cada posible movimiento, y Pacman elige el movimiento con la mejor puntuación.
