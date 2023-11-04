# ia-para-juegos
Repositorio de ia para el electivo "inteligencia artificial para videojuegos"

Proyecto originalmente hecho en python 2.X 
Traducción a python3 sacada del siguiente repositorio: https://github.com/jspacco/pac3man/tree/master/multiagent

Explicación de códigos para tarea 1. 

Question 1.
Mejoré la función de evaluación para crear un equilibrio entre la búsqueda activa de comida y la evasión  de los fantasmas. Utilizo la distancia de Manhattan, una medida simple y eficiente, para evaluar qué tan cerca está Pacman de la comida y los fantasmas asustados, otorgando recompensas basadas en esta proximidad. Para evitar que Pacman caiga en patrones repetitivos de huida (como estar dando vueltas sin sentido), he introducido una penalización significativa si un fantasma no asustado se encuentra demasiado cerca.  

Question 2.
Max Value() 
Representa la logica de decisión de Pacman. Se llama con el estado del juego y la profundidad actual de la búsqueda. 
Si el estado del juego es terminal (Pacman gana o pierde) o si se ha alcanzado la profundidad máxima (depth == 0), la función devuelve el valor de la función de evaluación para ese estado del juego.
Si no es un estado terminal y aún hay profundidad para explorar, se itera sobre todas las acciones legales de Pacman. Por cada acción, se genera el estado sucesor y se llama a  minValue() para el primer fantasma (agente 1), pasando el nuevo estado y la profundidad actual menos uno. 
La función busca el valor máximo entre los valores devueltos por minValue, que representa el mejor resultado posible para Pacman después de que todos los fantasmas hayan hecho su movimiento mas optimo.

Min Value()
Representa la lógica de decisión de los fantasmas en el juego. Se llama con el estado actual del juego, el índice del agente fantasma que está tomando la decisión, y la profundidad de búsqueda restante. Similar a la función maxValue(), si el estado del juego es un estado terminal (Pacman gana o pierde) o si la profundidad de búsqueda ha llegado a cero, la función retorna inmediatamente el valor calculado por la función de evaluación. En el caso de que aún haya acciones por explorar y la profundidad permitida no se haya agotado, minValue() procede a iterar sobre todas las acciones legales disponibles para el fantasma. Para cada acción, se genera un nuevo estado del juego, y dependiendo de si el agente actual es el último fantasma (es decir, su índice es igual al número total de agentes menos uno), se llama a la función maxValue() con el estado sucesor y una profundidad reducida en uno. Si aún quedan fantasmas por actuar, minValue() se llama a sí misma recursivamente para el siguiente fantasma, manteniendo la profundidad actual. La función busca el valor más bajo entre todos los valores devueltos por las llamadas subsiguientes, representando así el mejor resultado posible para los fantasmas, y por ende, el peor escenario para Pacman, bajo la suposición de que los fantasmas juegan de manera óptima."

getaction() itera sobre todas las acciones legales de Pacman desde el estado actual del juego. Para cada acción, genera el estado sucesor y llama a minValue para el primer fantasma. La acción que resulta en el mayor valor retornado por minValue es la acción que Pacman debería tomar. Esto porque según Minimax, Pacman quiere maximizar su mínimo beneficio garantizado, asumiendo que los fantasmas juegan óptimamente.
