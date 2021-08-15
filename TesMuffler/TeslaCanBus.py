#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-13"
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
    #TODO

except ImportError:
	print("Debug.py or GlobalConstant.py didn't import correctly, please verify that all files are in same directory as the TeslaCanBus.py file.")
	#TODO


class TeslaCanBus:

	#Debugging CONSTANTS
	DEBUG_STATEMENTS_ON = True

    FAST = 1000000  # 1 Mbit/sec (Mbps)
    SLOW = 20000    # 20 kbits/sec (kbps)
    
    def unitTest():
        model_S_Default = TeslaCanBus()
        model_S_Fast1 = TeslaCanBus(1, GC.MODEL_S, TeslaCanBus.FAST)
        model_S_Slow2 = TeslaCanBus(2, TeslaCanBus.SLOW)
        
        model_3_Default = TeslaCanBus()  
        assert readGasPedalPosition()  # THIS SHOULD FAIL 3 != S
        model_3_Default = TeslaCanBus(0, GC.MODEL_3)
        model_3_Fast1 = TeslaCanBus(1, GC.MODEL_3)
        model_3_Slow1 = TeslaCanBus(2, GC.MODEL_3, TeslaCanBus.SLOW)
        model_3_Slow0 = TeslaCanBus(0, GC.MODEL_3, TeslaCanBus.SLOW)
        
        calibrationObject = TeslaCalibration()
        model_Y_Default = TeslaCanBus(0, GS.MODEL_Y, TeslaCanBus.FAST, calibrationObject)
        # TODO model_y, cyberTruck, ATV, Roadster (IN THAT ORDER)
    
    def __init__(self, carModel=GC.MODEL_S, channel=0, bitrate=TeslaCanBus.FAST, calibrationObject=GC.DEFAULT_MAX_PEDAL_TRAVEL):

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(TeslaCanBus.DEBUG_STATEMENTS_ON, thisCodesFilename)
        
        self.CalibratedMaxPedalTravel = calibrationObject.getMaxPedalTravel()
        
        if(carModel == GC.MODEL_S):
            self.bus = can.interface.Bus(bustype=)
        elif(TODO):
        else:
        
        
    def readGasPedalPosition(units):
        data = TODO
        msg = can.Message(arbitration_id=0x7df, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], extended_id=False)
        sendMessage(msg)
        
        if(units == GS.PERCENTAGE):
            value = percentOfMax
        elif(units == GS.MILLIMETERS):
            value = percentOfMax * self.CalibratedMaxPedalTravel       
        elif(units == GS.CENTIMETERS):
        else:
        
        
        return value

    def readGasPedalVelocity():
        #TODO COPY readGasPedalPosition()
        
        
        return mmPerSec

    def readGasPedalVAcceleration():
        #TODO COPY readGasPedalPosition()
        
        return mmPerSecPerSec

    def sendMessage(self, msg):
        try:
            bus.send(msg)
            print("CAN Bus message sent on {}".format(bus.channel_info))
        except can.CanError:
            print("CAN Bus message was NOT sent")            


if __name__ == "__main__":
    
    unitTest()
    