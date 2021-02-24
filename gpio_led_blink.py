import RPi.GPIO as GPIO
import time

###########PIN DEFINICIONES#######################

pwmPin = 18
ledPin = 23
button = 17

dutyCiclo = 75

#SETUP GPIO /// ENTRADAS, SALIDAS Y PWM

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(pwmPin,GPIO.OUT)
GPIO.setup(button,GPIO.IN, pull_up_down = GPIO.PUD_UP) #Definimos el pin como pullup

pwm = GPIO.PWM(pwmPin, 200) #Iniciamos el pwm a una frecuencia de 200 hz

GPIO.output(ledPin,GPIO.LOW) # Ponemos el pin del led en 0
pwm.start(dutyCiclo) # Iniciamos el pwm con una frecuencia de 200 hz al 75%

try:
    
    while 1:
        
        if GPIO.input(button): #boton no precionado -> verdad 1 
        
            # sí el boton no está precionado
            # atenuar el rojo
        
            pwm.ChangeDutyCycle(dutyCiclo) #INCREMENTA EL PWM
            GPIO.output(ledPin, GPIO.LOW) #LED APAGADO
        
        else:
            
            #Sí el boton está precionado
            #parpadea el verde
            #atenua el rojo
            
            pwm.ChangeDutyCycle(dutyCiclo) # INCREMENTA EL PWM
            GPIO.output(ledPin, GPIO.HIGH) #EL LED PRENDE
            time.sleep(0.5) # ESPERA 500 MS
            pwm.ChangeDutyCycle(100 - dutyCiclo) #DECREMENTA EL PWM
            GPIO.output(ledPin, GPIO.LOW) # EL LED SE APAGA
            time.sleep(0.5) #ESPERA 500 Y REPITE LO DE ARRIBA
            
        
except KeyboardInterrupt:
    
    pwm.stop() #Detenemos el pwm
    GPIO.cleanup() #limpiamos la conf