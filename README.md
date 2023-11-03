# ia-para-juegos
Repositorio de ia para el electivo "inteligencia artificial para videojuegos"

Proyecto originalmente hecho en python 2.X 
Traducción a python3 sacada del siguiente repositorio: https://github.com/jspacco/pac3man/tree/master/multiagent

Explicación de códigos para tarea 1. 

Question 1.
En mi implementación mejorada del agente reflejo, he refinado la función de evaluación para crear un equilibrio entre la búsqueda activa de comida y la evasión inteligente de los fantasmas. Utilizo la distancia de Manhattan, una medida simple y eficiente, para evaluar qué tan cerca está Pacman de la comida y los fantasmas asustados, otorgando recompensas basadas en esta proximidad. Para evitar que Pacman caiga en patrones repetitivos de huida (como estar dando vueltas sin sentido), he introducido una penalización significativa si un fantasma no asustado se encuentra demasiado cerca.  
