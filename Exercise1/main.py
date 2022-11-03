#!/usr/bin/env pybricks-micropython
#This robot prints hello world, and then drives around in a square.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
Motor1 = Motor(Port.A)
Motor2 = Motor(Port.B)
robot = DriveBase(Motor1, Motor2, 20, 130)

ev3.speaker.beep()
ev3.screen.print("Hello World!")
wait(500)
for x in range(4):
    robot.straight(200)
    wait(500)
    robot.turn(94)
    wait(500)
ev3.speaker.play_file('niceDay.wav')
