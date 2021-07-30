#!/usr/bin/env python3
"""
__author__ =  "Blaze Sanders"
__email__ =   "blaze.d.a.sanders@gmail.com"
__status__ =  "Development"
__date__ =    "Late Updated: 2021-05-01"
__doc__ =     "Control the Parallax LASER rangefinder SKU #28041”
"""

# https://www.parallax.com/product/28041

# Used to control GPIO pins and control motors, servos, and relays
# https://gpiozero.readthedocs.io/en/stable/
import gpiozero

# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

# Useful CONSTANTS
DEBUG_STATEMENTS_ON = True
HIGH = 1
LOW = 0
CM = 'centimeter'

# LASER CONSTANTS
SPEED_OF_LIGHT = 299,792,458    # Units are meters per second
MAX_RANGE = 2                   # Units are meters
NO_OBJECT_WITHIN_2M_RANGE = -1


class LaserPING:
    ###
    # Constructor for LaserPING object
    #
    # @pinBCM - BCM PIN number LaserPING ?input? pin is connected to
    #
    # speedOfForCalculations
    def __init__(pinBCM):
        self.pinNumber = pinBCM
        self.pinObject = OutputDevice(pinBCM)
        self.speedOfLightForCalculations = SPEED_OF_LIGHT

def getDistance():
    """
    Get the distance to closet object in line with LASER pointer.

    return Distance to object in centimeters
    """

    startTime = time.TODO
    self.pinObject.value = LOW

    if(self.pinObject.value == HIGH):
        endTime = time.TODO
        totalTime = endTime - startTime
        distance = totalTime * self.speedOfLightForCalculations

    else:
       distance = NO_OBJECT_WITHIN_2M_RANGE

    return distance

###
# Adjust internal distance calculation if LASER is going through water or other weird environment
#
# @ratio - Number less than 1 used to calibrate laser for your environment
#
# return NOTHING
###
def adjustSpeedOfLigth(ratio):
    if(ratio > 1):
        print(“STOP TRYING TO BREAK PYSHICS!!!”)
    self.speedOfLightForCalculations *= ratio
    print(“New speed of light for calculations is “ + speedOfLightForCalculations + “ meters/sec”)

def debugPrint(stringToPrint):


if __name__ == “__main__”:
    print(“START LaserPING.py UNIT TEST”)

    print(“END LaserPING.py  UNIT TEST”)
