# IMPORT LIBRARIES
import RPi.GPIO as GPIO
import time

# CONFIGURE PYTHON WITH PI
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# PIN ASSIGNMENTS
#switchCW = 22 # CLOCKWISE SWITCH POSITION PIN (CONNECT TO SWITCH TERMINAL 1)
#switchCCW = 27 # COUNTERCLOCKWISE SWITCH POSITION PIN (CONNECT TO SWITCH TERMINAL 3)

DIR = 27 # DIRECTION GPIO PIN
PUL = 17 # PULSE GPIO PIN
ENA = 22 # ENABLE GPIO PIN

# CONFIGURE INPUT PINS
# SWITCH TERMINAL 2 GETS CONNECTED TO 3.3V SOURCE
#GPIO.setup(switchCW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(switchCCW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# CONFIGURE OUTPUT PINS
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

counter = 0

# CONFIGURE PWM CONTROL CHARACTERISTICS
frequencyPWM = 1600 # FREQUENCY OF PWM FROM PI (Hz)
dutycyclePWM = 50 # DUTY CYCLE OF PWM FROM PI (%)
PWM = GPIO.PWM(PUL, frequencyPWM) #CONFIGURE PUL PIN AS PWM
PPR = 3200 # PULSES PER REVOLUTION. DIP STICK MISCROSTEP SETTING ON DRIVER
RPS = frequencyPWM / PPR # REVS PER SECOND OF MOTOR SHAFT
print(RPS, 'REVOLUTIONS PER SECOND')

try:
    while True:
        if (counter % 2 == 0): # SWITCH IN CLOCKWISE POSITION?
            #print("Clockwise!") # TERMINAL FEEDBACK
            GPIO.output(ENA, False) # ENABLE THE MOTOR DRIVE
            GPIO.output(DIR, True) # SET DIRECTION PIN TO HIGH
            PWM.start(dutycyclePWM) # START PWM WITH 50% DUTY CYCLE
            time.sleep(0.2)
            counter = counter + 1
        elif (counter % 2 == 1): # SWITCH IN COUNTERCLOCKWISE POSITION?
            #print("Counterclockwise!") # TERMINAL FEEDBACK
            GPIO.output(ENA, False) # ENABLE THE MOTOT DRIVE
            GPIO.output(DIR, False) # SET DIRECTION PIN TO LOW
            PWM.start(dutycyclePWM) # START PWM WITH 50% DUTY CYCLE
            timel.sleep(0.2)
            counter = counter + 1
        time.sleep(0.1)
except KeyboardInterrupt: # PRESS CTRL-C TO TERMINATE THE SCRIPT
    print ("\nCtrl-C pressed. Stopping and exiting...")
finally:
    GPIO.output(PUL, False) # TURN OFF PWM GPIO
    GPIO.output(ENA, True) # DISABLE THE MOTOR DRIVE
    GPIO.cleanup()
