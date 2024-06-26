#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-18"
__doc__     = "Recalibrate zero point of hardware and sensors that MIGHT change over time from wear & tear"
"""

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# Allow pausing of code to let humans to read debug statements
# https://docs.python.org/3/library/time.html
import time

# Access internally developed libraries

# Generate a timestamped .txt data logging file and custom terminal debugging output
#from Debug import *

# Useful global constants used across all TesMuffler code
import GlobalConstants as GC

# TODO High
import Vehicle

# TODO CIRCULAR IMPORT????
#import TeslaCanBus


class TeslaCalibration:

    # Debugging CONSTANTS
    DEBUG_STATEMENTS_ON = True

    def unitTest():
        """ Run test using ALL publicly released Tesla model

        See __date__ at top of this file to determine valid models

        Arg(s):
            NONE

        Returns:
            Assert ??? if any test faile, NOTHING otherwise
        """
        TeslaModelS = Vehicle(GC.MODEL_S)
        testObject1 = TeslaModelS.TeslaCalibration()
        testObject1.runCalibration()

        testObject2 = TeslaCalibration()
        testObject1.runCalibration()


    def __init__(self, car, gasPedalMax=69, gasPedalMin=0, 
                 brakePedalMax=69, brakePedalMin=0,
                 speakerVolume=42):
        """Constructor to initialize a TeslaCalibration object, to recalibrate the zero point of 
           hardware and sensors that MIGHT change over time from wear & tear  # NOQA: 

        Args:
            gasPedalMax (int, optional): Physical location of the GAS pedal when a driver pushes the pedal to the 
                                         absolute BOTTOM as reported by Tesla internal software over the CAN bus. 
                                         Defaults to 69 millimeters.
            gasPedalMin (int, optional): Physical location of the GAS pedal when a driver does NOTHING to the pedal 
                                         as reported by Tesla internal software over the CAN bus. Defaults to 0.
            brakePedalMax (int, optional): Physical location of the BRAKE pedal when a driver pushes the pedal to the 
                                           absolute BOTTOM as reported by Tesla internal software over the CAN bus. 
                                           Defaults to 69 millimeters.
            brakePedalMin (int, optional): Physical location of the BRAKE pedal when a driver does NOTHING to the pedal 
                                           as reported by Tesla internal software over the CAN bus. Defaults to 0.
            speakerVolume (int, optional): Volume level from 0 to 11 ("These go to 11"Nigel Tufnel Spinal Tap). Defaults to 6.
        """

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(TeslaCalibration.DEBUG_STATEMENTS_ON, thisCodesFilename)
        
        # TODO Determine these using Twitter and Barklee's and Joe's Tesla's
        self.goPedalMax = 69 #gasPedalMax
        self.goPedalMax = 69 #gasPedalMin
        self.brakePedalMax = 69 #brakePedalMax
        self.brakePedalMin = 69 #brakePedalMin
        
        self.speakerVolume = speakerVolume
    
    # GETTERS
    def getGasPedalMax(self):
        return self.gasPedalMax

    def getGasPedalMin(self):
        return self.gasPedalMin

    def getBrakePedalMax(self):
        return self.brakePedalMax

    def getBrakePedalMin(self):
        return self.brakePedalMin
    
    # SETTERS
    def setGasPedalMax(self, model=GC.MODEL_S):
        self.gasPedalMax = self.Car.TeslaCanBus.readGasPedalPosition()

    def setGasPedalMin(self, minValue):
        self.gasPedalMin = minValue

    def setBrakePedalMax(self):
        print("TODO")

    def setBrakePedalMin(self, minValue):
        self.brakePedalMin = minValue

    def runCalibration():
        timeDelay = 0
        print("Please push GAS pedal all the way down and hold for AT LEAST ", GC.MAX_UI_DEALY, " seconds.")
        while(timeDelay < GC.MAX_UI_DEALY):
            print("..")
            time.sleep(GC.UI_TERMINAL_DELAY)  # Units are seconds
            timeDelay += GC.UI_TERMINAL_DELAY
            TeslaCalibration.setGasPedalMax()
        print("Release the GAS pedal now")
        time.sleep(1)

        print("Please push BRAKE pedal all the way down and hold for AT LEAST ", GC.MAX_UI_DEALY, " seconds.")
        while(timeDelay < GC.MAX_UI_DEALY):
            print(".")
            time.sleep(GC.UI_TERMINAL_DELAY)  # Units are seconds
            timeDelay += GC.UI_TERMINAL_DELAY
            TeslaCalibration.setBrakePedalMax()
        print("Release the BRAKE pedal now")
        time.sleep(1)


if __name__ == "__main__":

    TeslaCalibration.unitTest()
