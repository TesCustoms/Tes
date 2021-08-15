#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-14"
__doc__     = "Calibrate hardware and sensors that MIGHT change over time from wear & tear"
"""

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# Allow pausing of code to let humans to read debug statements
# https://docs.python.org/3/library/time.html
import time

# Access internally developed libraries
try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    import Debug

    # Useful global constants used across all TesMuffler code
    import GlobalConstant as GC

    # TODO CIRCULAR IMPORT????
    import TeslaCanBus

except ImportError:
    print("Debug.py or GlobalConstant.py didn't import correctly")
    print("Please verify that those files are in same directory as the TeslaCanBus.py")
    #TODO


class TeslaCalibration:

    # Debugging CONSTANTS
    DEBUG_STATEMENTS_ON = True

    def unitTest():
        testObject1 = TeslaCalibration()
        testObject1.runCalibration()

    def __init__(self, gasPedalMax=69, gasPedalMin=0, 
                 brakePedalMax=69, brakePedalMin=0,
                 speakerVolume=42):
        """[summary]

        Args:
            gasPedalMax (int, optional): [description]. Defaults to 69.
            gasPedalMin (int, optional): [description]. Defaults to 0.
            brakePedalMax (int, optional): [description]. Defaults to 69.
            brakePedalMin (int, optional): [description]. Defaults to 0.
            speakerVolume (int, optional): [description]. Defaults to 42.
        """

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(TeslaCalibration.DEBUG_STATEMENTS_ON, thisCodesFilename)
        
        # TODO Determine these using Twitter and Barklee's and Joe's Tesla's
        self.gasPedalMax = gasPedalMax
        self.gasPedalMin = gasPedalMin
        self.brakePedalMax = brakePedalMax
        self.brakePedalMin = brakePedalMin
        
        self.speakerVolume = speakerVolume
    
    def setGasPedalMax(self):
        self.gasPedalMax = TeslaCanBus.readGasPedalPosition()

    def setGasPedalMin(self):
        print("TODO")

    def setBrakePedalMax(self):
        print("TODO")

    def setBrakePedalMin(self):
        print("TODO")

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
            print("..")
            time.sleep(GC.UI_TERMINAL_DELAY)  # Units are seconds
            timeDelay += GC.UI_TERMINAL_DELAY
            TeslaCalibration.setBrakePedalMax()
        print("Release the BRAKE pedal now")
        time.sleep(1)


if __name__ == "__main__":

    TeslaCalibration.unitTest()
