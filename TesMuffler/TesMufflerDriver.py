#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-05-01"
__doc__     = "TesMuffler project code starts running here"
"""

FUNCTION_DELAY = 5 # Units are milliSeconds

# Allow CLI to pass parameters into this driver for testing
# https://docs.python.org/3/library/argparse.html
import argparse

# Allow program to extract filename of current file
# https://docs.python.org/3/library/os.html
import os

# Interface with Tesla ODB via CAN Bus
# https://python-can.readthedocs.io/en/2.1.0/index.html#
import can

# Interface with Parallax LASER rangefinder SKU #2801
from LaserPING import *

# Interface CPU with Tesla Bluetooth to produce engine sound
from EngineSoundGenerator import *


def configureCurrentSetup():
    maxDistance = 0     # Units are centimeters
    minDistance = 300   # Units are centimeters
    timeDelay = 0       # Units are milliSeconds
    while(timeDelay < 5000):
        currentDistance == LaserPing.getDistance()
        if(currentDistance >= minDistance):
            maxDistance = currentDistance

        if(currentDistance < minDistance):
            minDistance = currentDistance

        timeDelay = timeDelay + FUNCTION_DELAY

    return [minDistance, maxDistance]

if __name__ == "_main_":

    print("Press & release acclerator multiple times for the  next 5 seconds")
    [ZERO_THROTTLE, MAX_THROTTLE] = configureCurrentSetup()

    currentProgramFilename = os.path.basename(__file__)
    self.DebugObject = Debug(True, currentProgramFilename)

    defaultSound = SoundGenerator.DEFAULT_SOUND

    while(True):
        throttlePostion = LaserPing.getDistance()
        if(throttlePosition == ZERO_THROTTLE):
            EngineSoundGenerator.play()
        else:
            print("TODO")
