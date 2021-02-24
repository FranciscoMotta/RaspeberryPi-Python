import RPi.GPIO as GPIO #importamos la libreria del GPIO de la placa del raspberry
import time

######PIN DEFINITION#######

ledPinBlink = 23
buttonPinPullUp = 17

primeraVariable = True
segundaVariable = True

#########DECLARACION DE ENTRADAS Y SALIDAS ##########

GPIO.setmode(GPIO.BCM) # Nos referimos a los pines por su numero GPIO.BOARD tiene la misma funcion
GPIO.setup(ledPinBlink, GPIO.OUT) #Ponemos el pin 23 como salida
GPIO.setup(buttonPinPullUp, GPIO.IN, pull_up_down = GPIO.PUD_UP) #Configuramos el pin 17 como entrada pull-up

############INICIALIZACION DE PUERTOS################

GPIO.output(ledPinBlink, GPIO.LOW)


while 1:
    
    if GPIO.input(buttonPinPullUp): #Boton no pulsado
        
        GPIO.output(ledPinBlink, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(ledPinBlink, GPIO.LOW)
        time.sleep(0.1)
        while primeraVariable:
            print ("boton pulsado")
            primeraVariable = False
            segundaVariable = True
        
    else: #Boton pulsado
        
        GPIO.output(ledPinBlink, GPIO.LOW)
        while segundaVariable:
            print ("boton no pulsado")
            segundaVariable = False
            primeraVariable = True
        
        