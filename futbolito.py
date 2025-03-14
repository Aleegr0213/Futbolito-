import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground.bluefruit import cpb
from time import sleep
import digitalio

#Neopixels
cpb.pixels.brightness = 0.1 
cpb.pixels.fill((0,0,0)) 
cpb.pixels.show()

#Servomotores
pwm1 = pwmio.PWMOut(board.A6, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.TX, duty_cycle=2 ** 15, frequency =50)
my_servo1 = servo.Servo(pwm1)
my_servo2 = servo.Servo(pwm2)

#Sensores
porteria1 = board.A1  
porteria2 = board.A2
pared1 = board.A3
pared2 = board.A4

# Configurar el pin como entrada
porteria1_input = digitalio.DigitalInOut(porteria1)
porteria1_input.direction = digitalio.Direction.INPUT
porteria1_input.pull = digitalio.Pull.UP  

porteria2_input = digitalio.DigitalInOut(porteria2)
porteria2_input.direction = digitalio.Direction.INPUT
porteria2_input.pull = digitalio.Pull.UP  

pared1_input = digitalio.DigitalInOut(pared1)
pared1_input.direction = digitalio.Direction.INPUT
pared1_input.pull = digitalio.Pull.UP 

pared2_input = digitalio.DigitalInOut(pared2)
pared2_input.direction = digitalio.Direction.INPUT
pared2_input.pull = digitalio.Pull.UP  

#directorios
colores = {"rojo":(255,0,0), "verde":(0,255,0), "azul":(0,0,255), "amarillo":(255,255,0), "rosa":(255,0,255)}

def inicio():
    cpb.play_tone(440, 0.2)
    cpb.play_tone(523, 0.1)
    cpb.play_tone(659, 0.1)
    cpb.play_tone(784, 0.1)
    cpb.play_tone(659, 0.1)
    cpb.play_tone(523, 0.1)

def control():
    angulo_minimo_x = 90
    angulo_maximo_x = 105
    angulo_minimo_y = 60
    angulo_maximo_y = 103
    x, y, z = cpb.acceleration
    sleep(0.1)
    angulo_x = int(angulo_minimo_x + ((((x+10)*100)/20) / 100) * (angulo_maximo_x - angulo_minimo_x))
    print("x", angulo_x)
    angulo_y = int(angulo_minimo_y + ((((y+10)*100)/20) / 100) * (angulo_maximo_y - angulo_minimo_y))
    print("y", angulo_y)
    my_servo1.angle = angulo_x
    my_servo2.angle = angulo_y
  
def perder():
    print("Perdiste")
    cpb.pixels.fill(colores["rojo"])
    cpb.pixels.show()
    cpb.play_tone(220, 0.2)
    cpb.play_tone(262, 0.2)
    cpb.play_tone(294, 0.2)
    cpb.play_tone(349, 0.2)
    cpb.play_tone(392, 0.2)  
    cpb.pixels.fill((0, 0, 0))
    cpb.pixels.show()
    sleep(1)

def gol():
    print("Gol")
    cpb.pixels.fill(colores["verde"])
    cpb.pixels.show()
    cpb.play_tone(659, 0.2)
    cpb.play_tone(784, 0.1)
    cpb.play_tone(1046, 0.1)
    cpb.play_tone(1175, 0.1)
    cpb.play_tone(1046, 0.1)
    cpb.play_tone(784,0.1)
    cpb.pixels.fill((0, 0, 0))
    cpb.pixels.show()
    sleep(1)

def ganar(x):
    print("Ganaste")
    cpb.pixels.fill(colores[x])
    cpb.pixels.show()
    cpb.play_tone(659, 0.2)
    cpb.play_tone(784, 0.1)
    cpb.play_tone(1046, 0.1)
    cpb.play_tone(1175, 0.1)
    cpb.play_tone(1046, 0.1)
    cpb.play_tone(784,0.1)
    cpb.pixels.fill((0, 0, 0))
    cpb.pixels.show()
    sleep(1)

def contador_1(cantidad):
    if cantidad>0:
        for i in range(min(cantidad, 5)):
            cpb.pixels[i]= colores["azul"]

def contador_2(cantidad):
    if cantidad>0:
        for i in range(5, 5 + min(cantidad, 5)):
            cpb.pixels[i]= colores["amarillo"]

#Variables
puntos_jugador1 = 0
puntos_jugador2 = 0

print("Inicializando")
x = False
if cpb.button_a:
    x = True
while x:
    if cpb.switch:
        cpb.red_led = True
        print("Jugador 1")
        contador_1(puntos_jugador1)
        contador_2(puntos_jugador2)
        control()
        if porteria1_input == False:
            gol()
            puntos_jugador1 = puntos_jugador1 + 1
            puntos_jugador2 = puntos_jugador2 - 1

        elif pared1_input == False:
            perder()
            puntos_jugador1 = puntos_jugador1 - 1
            puntos_jugador2 = puntos_jugador2 + 1
        
        elif puntos_jugador1 == 5:
            ganar("azul")
            x = False

    else:
        print("Jugador 2")
        contador_1(puntos_jugador1)
        contador_2(puntos_jugador2)
        control()
        if porteria2_input == False:
            gol()
            puntos_jugador1 = puntos_jugador1 - 1
            puntos_jugador2 = puntos_jugador2 + 1

        elif pared2_input == False:
            perder()
            puntos_jugador1 = puntos_jugador1 + 1
            puntos_jugador2 = puntos_jugador2 - 1
        
        elif puntos_jugador2 == 5:
            ganar("amarrillo")
            x = False