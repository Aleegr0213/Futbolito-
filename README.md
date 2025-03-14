# Futbolito-
Código para un juego interactivo utilizando la tarjeta Circuit Playground Bluefruit. Se controlan servomotores mediante el acelerómetro, se detectan eventos con sensores digitales y se usan los Neopixels para retroalimentación visual. El código permite jugar en modo de dos jugadores con detección de goles y colisiones.
# CircuitPlayground Bluefruit Game 🎮

Este es un juego interactivo desarrollado para la **Adafruit Circuit Playground Bluefruit**. Utiliza los sensores y actuadores de la tarjeta para crear una experiencia de juego basada en movimiento y luces.

## 🔧 Características
- Control de **servomotores** con el acelerómetro
- Uso de **Neopixels** para indicar estados del juego
- Detección de **goles** y **colisiones** con sensores digitales
- Soporte para **dos jugadores**
- Sonidos con el buzzer incorporado

## 🚀 Instalación
1. Instala [CircuitPython](https://circuitpython.org/board/circuitplayground_bluefruit/) en tu placa.
2. Copia el archivo `game.py` al directorio raíz de la tarjeta.
3. Instala las bibliotecas necesarias en la carpeta `lib` de la tarjeta:
   ```bash
   pip install adafruit-circuitpython-motor adafruit-circuitpython-circuitplayground


