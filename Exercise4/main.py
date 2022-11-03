#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import threading

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
######################################################
#          DENNE KODEN SVINGER PÅ SVART              #
######################################################

# Create your objects here.
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

def høyre():
    turnRate = 0
    while(True):
        measuredH = høyreSensor.reflection()
        if (measuredH < 65):
            turnRate = turnRate + 1
            while (measuredH < 65):
                measuredV = venstreSensor.reflection()
                if measuredV < 65:
                    base.drive(175, 0)
                    turnRate = 0
                elif (turnRate < 60): #Før: 60
                    turnRate = turnRate + 1
                    base.drive(125, turnRate) #100 fungerer
                measuredH = høyreSensor.reflection()
            turnRate = 0
            base.drive(175, 0)


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
            

base.drive(175,0)
threadH = threading.Thread(target=høyre, args=())
threadV = threading.Thread(target=venstre, args=())
threadH.start()
threadV.start()

while (not startButton.pressed()):
    continue
wait(19500)
dirtyTricks.run_time(45, 2000)
while(True):
    wait(5)
