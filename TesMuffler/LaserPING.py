#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "blaze.d.a.sanders@gmail.com"
__company__ = "Humanity"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-06-17"
__doc__ =     "Control the Parallax LASER rangefinder sensor”

# https://www.parallax.com/product/28041

# Used to control GPIO pins and control motors, servos, and relays 
import gpiozero

# Used to control the space-time fabric :)
import time      

# Useful CONSTANTS 
DEBUG_STATEMENTS_ON = True
HIGH = 1
LOW = 0
CM = “centimeter”
IN = “inch”


# LASER CONSTANTS 
SPEED_OF_LIGHT = 299,792,458 # Units are m/s

class LaserPING:


###
# Constructor for LaserPING object
#
# @pinBCM - BCM PIN number LaserPING ?input? pin is connected to 
# 
# speedOfForCalculations 
def __init__(pinBCM):
    self.pin = pinBCM
    self.speedOfLightForCalculations = SPEED_OF_LIGHT

###
# Get the distance to closet object in line with LASER pointer. 
# 
# @units - Units distance will be returned in (e.g. centimeter or inches)
#
# return Distance to object in selected units 
###
def getDistance(units):
    if(units == CM)):
        distance = 
    elif(units == IN):
        distance = 
    else:
        print(“INCORRECT units PARAMETER PASSED TO getDistance() FUNCTION. TRY CM OR IN”)

    return distance

###
# Adjust internal distance calculation if LASER is going through water or other weird environment
#
#
# return NOTHING
###
def adjustSpeedOfLigth(ratio):

def debugPrint(stringToPrint):


if __name__ == “__main__”:
    print(“START LaserPING.py UNIT TEST”)

    print(“END LaserPING.py  UNIT TEST”)
