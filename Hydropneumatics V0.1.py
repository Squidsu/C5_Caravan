#Code for automatic height adjustment of Citroen C5 caravan project.
#Coded by Squidtec Services © for Hannah Customs Andover ©
#Completed Version 0.1 23/04/2020

import RPi.GPIO as GPIO #Import all libraries required for this script
import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)   #This code takes the output from the arduino
while 1:                                    #and puts it on the Raspberry Pi
    if(ser.in_waiting >0):
        line = ser.readline()
        print(line)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to lower vehicle to GPIO23
GPIO.setup(24, GPIO.OUT) #Output for relay for raising vehicle to GPIO24
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to raise vehicle to GPIO2
GPIO.setup(25, GPIO.OUT) #Output for relay for lowering vehicle to GPIO25
GPIO.setup(12, GPIO.OUT) #Output for warning buzzer to GPIO12

X = 1   #System where 1 is low 2 is ride height and 3 is service height

while True:
    if GPIO.input(2) == GPIO.HIGH: #If raise button is pushed add 1 to X
        X + 1

    if GPIO.input(23) == GPIO.HIGH: #If lower button is pushed subtract 1 from X
        X - 1

if X < 1:       #This piece of code beeps a buzzer and prevents X
    X == 1      #From going below 1 where there is no height setting and the code would stop working
    GPIO.output(12, True)
    time.sleep(1)
    GPIO.output(12, False)

if X > 3:       #This piece of code beeps a buzzer and prevents X from going
    X == 3      #Above 3 where the code would also not work
    GPIO.output(12, True)
    time.sleep(1)
    GPIO.output(12, False)

if X == 1:      #This is the lowest suspension setting for the caravan
    while line < 1.1:   #Keeps the car between a voltage range from the sensor
        GPIO.output(24, True)
        else:
            GPIO.output(24, False)
    while line > 1.3:
        GPIO.output(25, True)
        else:
            GPIO.output(25, False)

if X == 2:      #This is the ride height setting for the caravan
    while line < 2.1:   #Keeps the car between a voltage range from the sensor
        GPIO.output(24, True)
        else:
            GPIO.output(24, False)
    while line > 2.3:
        GPIO.output(25, True)
        else:
            GPIO.output(25, False)

if X == 3:      #This is the service height setting for the caravan
    while line < 3.1:   #Keeps the car between a voltage range from the sensor
        GPIO.output(24, True)
        else:
            GPIO.output(24, False)
    while line > 3.3:
        GPIO.output(25, True)
        else:
            GPIO.output(25, False)
