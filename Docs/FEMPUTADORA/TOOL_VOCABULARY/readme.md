<h1 align="center"> FelipedelosH </h1>
<br>
<h4>Femputadora - Sistema de Vectorización Semántica</h4>

![Banner](Docs/banner.png)
<br>
:construction: Status of project :construction:
<br><br>
Femputadora es un motor de **vectorización semántica** que convierte texto en español en representaciones vectoriales de ? dimensiones contextuales. Cada palabra actúa como un **"Iterador Contextual"** que activa dimensiones específicas del significado.

## Conceptos Básicos

## Dimensión Semántica
Es una posición/coordenada en el espacio de significado.
Osea cada palabra va a formar un arreglo de (0,1) de que tanto se relaciona con otras palabras.

Ejemplo supongamos 2 dimensiones: 

Sujeto: [yo, otro]
Verbos: [hacer, dormir]

Entonces existen 4 dimenciones... que van a tener 4 iteradores contextuales.


## Iterador Contextual
Es la cantidad de opciones posibles... forma una arreglo dependiendo de las opciones.
Ejemplo:

"YO": [1,0,0,0]
"otro": [0,1,0,0]
"hacer": [0,0,1,0]
"dormir": [0,0,0,1]

Ahora bien la dimensión es dificil de comprender así... por ello vamos a verla con ejemplos:

"Yo me quede dormido": [1,0,0,1]
"Ella no puede hacerlo": [0,0,1,0]
"otro dia se hará": [0,1,1,0]

Dimensiones de las frases:

- Sujeto: quién realiza la acción.
- Verbo: la acción o estado. Pero los verbos son muchos; hay que agrupar o sacar los más comunes.
- Tiempo: pasado, presente, futuro.
- Lugar: dónde ocurre.
- Tema: trabajo, finanzas, salud, sueños, relaciones, etc.
- Emocion: alegría, tristeza, enojo, etc.
- Intensidad: palabras como muy, poco...
- Negación: palabras cono NO o NUNCA invierten el significado.


## :hammer:Funtions:

- `Function 1`: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.<br>
- `Function 2`: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.<br>
- `Function 3`: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.<br>
- `Function 3a`: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.<br>
- `Function 4`: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.<br>


## :play_or_pause_button:How to execute a project

Double click

## :hammer_and_wrench:Tech.

- code programing
- framework

## :warning:Warning.

- limitations.

## Autor

| [<img src="https://avatars.githubusercontent.com/u/38327255?v=4" width=115><br><sub>Andrés Felipe Hernánez</sub>](https://github.com/felipedelosh)|
| :---: |