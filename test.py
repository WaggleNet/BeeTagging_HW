import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#PIN Assignments (!!!temporary setup, adjust according to actual schematic!!!)
DIR = 27
PUL = 17
ENA = 22

#Configure Output Pins
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

#internal counter for testing 
counter = 0
stepRate = 10

#motor motion
#
#The following code repeats infinite times until termination.
#Linear Actuator moves back and forward

while True:
    if(counter % 2 == 0):
        GPIO.output(DIR, True)
        GPIO.output(ENA, True)
        for i in range(300):
           GPIO.output(PUL, True)
           time.sleep(1/200)
           GPIO.output(PUL, False)
           time.sleep(1/200)
        counter = counter + 1
    elif(counter % 2 ==1):
        GPIO.output(DIR, False)
        GPIO.output(ENA, False)
        for i in range(300):
           GPIO.output(PUL, True)
           time.sleep(1/200)
           GPIO.output(PUL, False)
           time.sleep(1/200)
        counter = counter + 1
