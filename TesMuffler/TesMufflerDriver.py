#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "N/A"
__status__  = "Development"
__date__    = "Late Updated: 2021-04-27"
__doc__     = "TesMuffler project code starts running here"
"""

# Allow CLI to pass parameters into this driver for testing
import argparse

# Allow program to extract filename of current file
import os

# Interface with Parallax LASER rangefinder
from LaserPing import *

# Interface CPU with Tesla Bluetooth to produce engine sound
from EngineSoundGenerator import *

# Interface with Tesla ODB over ??? CAN Bus
from OBD import *


def configure():
    maxDistance = 0
    minDistance = 300 #
    timeInMilliSeconds = 0
    while(timeInMilliSeconds < 5000)
        currentDistance == LaserPing.getDistance()
        if(currentDistance >= minDistance):
            maxDistance = currentDistance

        if(currentDistance < minDistance):
            minDistance = currentDistance

        time = time + 


    return [minDistance, maxDistance]

if __name__ == "_main_":

    print("Press & release acclerator multiple times for the  next 5 seconds")
    [ZERO_THROTTLE, MAX_THROTTLE] = configure()

    currentProgramFilename = os.path.basename(__file__)
    self.DebugObject = Debug(True, currentProgramFilename)

    defaultSound = SoundGenerator.DEFAULT_SOUND

    while(True):
        throttlePostion = LaserPing.getDistance()
        if(throttlePosition == ZERO_THROTTLE):
            EngineSoundGenerator.play()
        else:
            
