#!/usr/bin/env pybricks-micropython
#This robot is a slightly more advanced line-following robot, which was used to compete against other robots on a track. 
#The robot was quite robust, and made semi finals. It was sadly too slow to win. 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import threading

ev3 = EV3Brick()
høyreSensor = ColorSensor(Port.S1)
venstreSensor = ColorSensor(Port.S2)
hMotor = Motor(Port.A)
vMotor = Motor(Port.B)
dirtyTricks = Motor(Port.C)
base = DriveBase(vMotor, hMotor, 56, 70)
startButton = TouchSensor(Port.S3)

# Write your program here.
red = 45
green = 45
blue = 45
#A function for the right side sensor. Causes the robot to turn right if it picks up on the right sensor, but not the left. Turn rate increases, and caps out at 60 degrees.
def høyre():
    turnRate = 0
    while(True):
        measuredH = høyreSensor.reflection()
        if (measuredH < 65):
            turnRate = turnRate + 1
            while (measuredH < 65):
                measuredV = venstreSensor.reflection()
                if measuredV < 65:
                    base.drive(125, 0)
                    turnRate = 0
                elif (turnRate < 60)
                    turnRate = turnRate + 1
                    base.drive(125, turnRate)
                measuredH = høyreSensor.reflection()
            turnRate = 0
            base.drive(175, 0)

#A function for the left side sensor. Does the same thing as the previous function, but for the left side. 
#Can perform sharper turns than the right side due to the track going counterclockwise.
def venstre():
    turnRate = 0
    while(True):
        measuredV = venstreSensor.reflection()
        if measuredV < 65:
            turnRate = turnRate - 2
            while (measuredV < 65):
                measuredH = høyreSensor.reflection()
                if (measuredH < 65):
                    base.drive(125, 0)
                    turnRate = 0
                elif (turnRate > -75): #Før: -60
                    turnRate = turnRate - 1
                    base.drive(125, turnRate) #100 fungerer
                measuredV = venstreSensor.reflection()
            turnRate = 0
            base.drive(175, 0)
            
#The program runs the sensors in separate threads, increasing speed and making the code a bit easier to understand. 
base.drive(175,0)
threadH = threading.Thread(target=høyre, args=())
threadV = threading.Thread(target=venstre, args=())
threadH.start()
threadV.start()
#dirtyTricks is essentially a bucket of small lego pieces that was emptied onto the track to sabotage other robots. 
while (not startButton.pressed()):
    continue
wait(19500)
dirtyTricks.run_time(45, 2000)
while(True):
    wait(5)
