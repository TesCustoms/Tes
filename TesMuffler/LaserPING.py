# Used to control GPIO pins and control motors, servos, and relays 
import gpiozero

# Used to control the space-time fabric :)
import time      

# Useful CONSTANSTS 
DEBUG_STATEMENTS_ON = True
HIGH = 1
LOW = 0
CM = “centimeter”
IN = “inch”


# LASER CONSTANTS 
SPEED_OF_LIGHT = 299,792,458 # Units are m/s

class LaserPING:

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

def adjustSpeedOfLigth():

def debugPrint(stringToPrint):


if __name__ == “__main__”:
    print(“START LaserPING.py UNIT TEST”)

    print(“END LaserPING.py  UNIT TEST”)
