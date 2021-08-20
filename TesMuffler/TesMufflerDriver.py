#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-05-01"
__doc__     = "TesMuffler project code starts running here"
"""

# Allow CLI to pass parameters into this driver for testing
# https://docs.python.org/3/library/argparse.html
import argparse

# Allow program to extract filename of current file
# https://docs.python.org/3/library/os.html
import os

# Allow data from iOS and Android Firebase database to be accessed via API
# https://docs.python.org/3/library/json.html
import json
# https://github.com/thisbejim/Pyrebase
# TODO UNCOMMENT import pyrebase

# Interface CPU with Tesla Bluetooth to produce engine sound
# http://www.mega-nerd.com/SRC/
from EngineSoundGenerator import *

# 
import GlobalConstant as GC

# JSON stuff???
from io import StringIO

LASER_PIN = 0 #GPIO_0


def calibrateLaserSetup():
    """
    Runs a calibration process to ensure that hardware has not moved and that the zero and max throttle points are defined and within LASER's range.

    Key arguments:
    NONE

    Return value:
    [ZERO_THROTTLE, MAX_THROTTLE] a tuple defining the distance to the zero and max throttle pedal positions
    """

    maxDistance = 0     # Units are centimeters
    minDistance = 300   # Units are centimeters
    timeDelay = 0       # Units are milliSeconds
    while(timeDelay < 5000):
        currentDistance == LaserPing.getDistance()
        if(currentDistance >= minDistance):
            maxDistance = currentDistance

        if(currentDistance < minDistance):
            minDistance = currentDistance

        timeDelay = timeDelay + GC.FUNCTION_DELAY

    return [minDistance, maxDistance]



if __name__ == "__main__":

    #QR code on box links mobile app to your hardware with SMS 2FA 

    config = { "apiKey": "apiKey",
               "authDomain": "projectId.firebaseapp.com",
               "databaseURL": "https://databaseName.firebaseio.com",
               "storageBucket": "projectId.appspot.com",
               "serviceAccount": "path/to/serviceAccountCredentials.json"
             }

    firebase = pyrebase.initialize_app(config)
    
    
    io = StringIO()
    json.dump(['streaming API'], io)
    io.getvalue()

    '["streaming API"]'
    
    usersCarModel = json.get()
    
    try:
        BluetoothObject = BluetoothSetup(usersCarModel)
    except InvalidModelException:
        BluetoothObject = BluetoothSetup(BluetoothSetup.ALL) 
    
    
    
    print("Press & release acclerator multiple times for the  next 5 seconds")
    [ZERO_THROTTLE, MAX_THROTTLE] = calibrateLaserSetup()

    currentProgramFilename = os.path.basename(__file__)
    self.DebugObject = Debug(True, currentProgramFilename)

    defaultSound = SoundGenerator.DEFAULT_SOUND

    while(True):
        throttlePostion = LaserPing.getDistance()
        if(throttlePosition == ZERO_THROTTLE):
            EngineSoundGenerator.play()
        else:
            print("TODO")
