#!/usr/bin/env pybricks-micropython
#This robot is a simple line following robot. If the colour sensor detects black, it turns towards the sensor that picked it up. 
#It stops every 10 seconds and does a random text-to-speech joke out of 4 possible. 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import random

ev3 = EV3Brick()
høyreSensor = ColorSensor(Port.S1)
venstreSensor = ColorSensor(Port.S2)
ultSensor = UltrasonicSensor(Port.S3)
hMotor = Motor(Port.A)
vMotor = Motor(Port.B)
base = DriveBase(vMotor, hMotor, 56, 70)

lastTime = time.time()
red = 14
green = 14
blue = 14
joke1 = "What kind of tea is hard to swallow? Reality"
joke2 = "What's the best thing about Switzerland? I don't know, but the flag is a big plus"
joke3 = "Why do bees have sticky hair? They use honeycombs."
joke4 = "What do you call a fly with no wings? A walk."
jokes = (joke1, joke2, joke3, joke4)

ev3.speaker.set_volume(100, which='_all_')
run = True
while run:
    base.drive(150, 0)
    #Drives for 10 seconds
    while True:
        (hRed, hGreen, hBlue) = høyreSensor.rgb()
        if hRed < red or hGreen < green or hBlue < blue:
            base.turn(10)
            base.drive(150, 0)
        (vRed, vGreen, vBlue) = venstreSensor.rgb()
        if vRed < red or vGreen < green or vBlue < blue:
            base.turn(-10)
            base.drive(150,0)
        #Checks for obstacles with ultrasonic sensor
        if ultSensor.distance() < 100:
            run = False
            break
        currentTime = time.time()
        if currentTime - lastTime >= 10:
            break
    #"Entertains" the audience with poor jokes
    base.stop()
    if run:
        ev3.speaker.say(jokes[random.randint(0,3)])
        wait(500)
        lastTime = time.time()
ev3.speaker.play_file('fanfare.wav')





