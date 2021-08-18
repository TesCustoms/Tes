#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-17"
__doc__     = "Read only class for the OBD-II Tesla CAN Bus"
"""

# Interface with Tesla CAN bus via a ODB-II port adapter
# https://python-can.readthedocs.io/en/2.1.0/index.html#
# https://teslatap.com/modifications/extracting-internal-vehicle-data/
# https://www.obdlink.com/products/obdlink-mxp/
import can

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# Access internally developed libraries
try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    from Debug import *

    # Useful global constants used across all TesMuffler code
    import GlobalConstant as GC

    # Calibrate hardware and sensors that MIGHT change over time from wear & tear
    from TeslaCalibration import *
    #TODO

except ImportError:
    print("Debug.py, GlobalConstant.py, or TeslaCalibration.py didn't import correctly")
    print("Please verify that those files are in same directory as the TeslaCanBus.py")
    #TODO


class TeslaCanBus:
    TODO = -1
    
    # Debugging CONSTANTS
    DEBUG_STATEMENTS_ON = True

    FAST = 1000000  # 1 Mbit/sec (Mbps)
    SLOW = 20000    # 20 kbits/sec (kbps)

    def unitTest():
        model_S_Default = TeslaCanBus()
        model_S_Fast1 = TeslaCanBus(1, GC.MODEL_S, TeslaCanBus.FAST)
        model_S_Slow2 = TeslaCanBus(2, TeslaCanBus.SLOW)

        model_3_Default = TeslaCanBus()
        assert readGasPedalPosition()                                  # THIS SHOULD FAIL 3 != S
        model_3_Default = TeslaCanBus(0, GC.MODEL_3)
        model_3_Fast1 = TeslaCanBus(1, GC.MODEL_3)
        model_3_Slow1 = TeslaCanBus(2, GC.MODEL_3, TeslaCanBus.SLOW)
        model_3_Slow0 = TeslaCanBus(0, GC.MODEL_3, TeslaCanBus.SLOW)

        calibrationObject = TeslaCalibration()
        model_Y_Default = TeslaCanBus(0, GS.MODEL_Y, TeslaCanBus.FAST, calibrationObject)
        # TODO model_y, cyberTruck, ATV, Roadster (IN THAT ORDER)

    def __init__(self, carModel=GC.MODEL_S, channel=0, bitrate=TeslaCanBus.FAST,
                 calibrationObject=GC.DEFAULT_MAX_GAS_PEDAL_TRAVEL):

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(TeslaCanBus.DEBUG_STATEMENTS_ON, thisCodesFilename)

        self.CalibratedMaxGasPedalTravel = calibrationObject.gasPedalMax()
        self.CalibratedMaxBrakePedalTravel = calibrationObject.brakePedalMax()

        # TODO Test if each model and year has a different interface
        if(carModel == GC.MODEL_S):
            self.bus = can.interface.Bus(bustype=)
        elif(carModel == GC.MODEL_3):
        elif(carModel == GC.MODEL_X):
        elif(carModel == GC.MODEL_Y):
        
        
        

    def readGasPedalPosition(self, units):
        # command to request CAN bus to return pedal position
        command = TODO
        
        return canBusPedalSubroutine(GAS_PEDAL, command, units)

    def readGasPedalVelocity(self, units):
        # command to request CAN bus to return pedal position
        command = TODO
        
        data = canBusPedalSubroutine(GAS_PEDAL, command, units)
        
        mmPerSec = data * TODO
        
        return mmPerSec

    def readGasPedalVAcceleration():
        # command to request CAN bus to return pedal position
        command = TODO
        
        data = canBusPedalSubroutine(GAS_PEDAL, command, units)
        
        mmPerSecPerSec = data * TODO
        
        return mmPerSecPerSec

    
    def canBusPedalSubroutine(pedalType, command, units=GC.PERCENTAGE):
        msg = can.Message(arbitration_id=0x7df, command=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], extended_id=False)
        rawValue = sendMessage(msg)

        if(pedalType == GAS_PEDAL):
            percentOfMax = rawValue/GC.MAX_GAS_PEDAL_VALUE
            if(units == GS.PERCENTAGE):
                value = percentOfMax
            elif(units == GS.MILLIMETERS):
                value = percentOfMax * self.CalibratedMaxGasPedalTravel       
            elif(units == GS.CENTIMETERS):
                value = percentOfMax * (self.CalibratedMaxGasPedalTravel/10)
                
        elif(pedalType == BRAKE_PEDAL):
            percentOfMax = rawValue/GC.MAX_BRAKE_PEDAL_VALUE
            if(units == GS.PERCENTAGE):
                value = percentOfMax
            elif(units == GS.MILLIMETERS):
                value = percentOfMax * self.CalibratedMaxBrakePedalTravel       
            elif(units == GS.CENTIMETERS):
                value = percentOfMax * (self.CalibratedMaxBrakePedalTravel/10)
        
        else:
            self.DebugObject.Lprint("ERROR: Invalid pedal type was passed to a TeslaCanBus.py function")
        
        return value
    
    
    def sendMessage(self, msg):
        try:
            bus.send(msg)
            self.DebugObject.Dprint("CAN Bus message sent on {}".format(bus.channel_info))
        except can.CanError:
            self.DebugObject.Dprint("CAN Bus message was NOT sent")            


if __name__ == "__main__":

    unitTest()
