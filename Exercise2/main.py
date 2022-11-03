#!/usr/bin/env pybricks-micropython
#This is a "lawn mower" robot. It drives in a straight line until it bumps into something, then it reverses and turns slightly before continuing.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
motor1 = Motor(Port.A)
motor2 = Motor(Port.B)
avPå = TouchSensor(Port.S1)
bumpSensor = TouchSensor(Port.S2)
driveBase = DriveBase(motor1, motor2, 56, 100)

while not avPå.pressed():
    continue
ev3.speaker.set_volume(100, which='_all_')
ev3.speaker.say("Exercise 2")
driving = True
while not avPå.pressed():
    driveBase.drive(50, 0)
    while not bumpSensor.pressed():
        if avPå.pressed():
            driving = False
            break
        continue
    driveBase.stop()
    if driving:
        driveBase.straight(-100)
        driveBase.turn(45)
ev3.speaker.say("Exercise done")


