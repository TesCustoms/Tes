#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-18"
__doc__     = "Read only class for the OBD-II Tesla CAN Bus"
"""

# Interface with Tesla CAN bus via a ODB-II port adapter
# https://python-can.readthedocs.io/en/2.1.0/index.html#
# https://teslatap.com/modifications/extracting-internal-vehicle-data/
# https://www.obdlink.com/products/obdlink-mxp/
import can as canBus
#import can-isotp as canBus https://github.com/pylessard/python-can-isotp

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# TODO MIGHT NOT NEED THIS 
# https://docs.python.org/3/library/math.html
import math

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

    FAST = 1_000_000  # 1 Mbit/sec (Mbps)
    DEFAULT = 50_000  # 500 kbits/sec (kbps)
    SLOW = 20_000     # 20 kbits/sec (kbps)

    def unitTest():
        calibrationObject = TeslaCalibration(GC.MODEL_S)
        
        model_S_Default = TeslaCanBus(calibrationObject)
        assert model_S_Default.redGasPedalPosition()
        
        model_S_Fast1 = TeslaCanBus(1, GC.MODEL_S, TeslaCanBus.FAST, calibrationObject)
        # TODO
        
        model_S_Slow2 = TeslaCanBus(2, TeslaCanBus.SLOW, calibrationObject)
        #TODO 
        
        model_3_BAD = TeslaCanBus()
        assert model_3_BAD.readGasPedalPosition(), "Failed successfully! Unit Test tried to initialize a Model 3 as a Tesla Model S"
        
        model_3_Default = TeslaCanBus()
        assert TeslaCanBus.readGasPedalPosition(), "Default software initalization of Model S CAN bus, failed on Model 3 hardware"   # NOQA: E501                                 # THIS SHOULD FAIL 3 != S
        
        model_3_Fast1 = TeslaCanBus(1, GC.MODEL_3, TeslaCanBus.FAST)
        #TODO
        
        model_3_Slow1 = TeslaCanBus(2, GC.MODEL_3, TeslaCanBus.SLOW)
        #TODO
        
        model_3_Slow0 = TeslaCanBus(0, GC.MODEL_3, TeslaCanBus.SLOW)
        # TODO 
    
        model_Y_Default = TeslaCanBus(0, GS.MODEL_Y, TeslaCanBus.DEFAULT, calibrationObject)
        # TODO
        
        # TODO model_y, cyberTruck, ATV, Roadster (IN THAT ORDER)


    def __init__(self, year=2019, carModel=GC.MODEL_S, channel=0, bitrate=DEFAULT, calibrationObject=GC.DEFAULT_MAX_GAS_PEDAL_TRAVEL):

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(TeslaCanBus.DEBUG_STATEMENTS_ON, thisCodesFilename)

        self.CalibratedMaxGasPedalTravel = calibrationObject.gasPedalMax()
        self.CalibratedMaxBrakePedalTravel = calibrationObject.brakePedalMax()
        
        if(carModel == GC.MODEL_S and year >= 2020):  #TODO Check years supported
            self.bus = canBus.interface.Bus(bustype=TODO)
        elif(carModel == GC.MODEL_3 and year >= 2019):
            self.bus = canBus.interface.Bus(bustype=TODO)
        elif(carModel == GC.MODEL_X and year >= 2020):  #TODO Check years supported
            self.bus = can.interface.Bus(bustype=TODO)
        elif(carModel == GC.MODEL_Y and year >= 2020):  #TODO Check years supported
            self.bus = can.interface.Bus(bustype=TODO)
        elif(carModel == GC.CYBER_TURCK and year >= 2022):  #TODO Check years supported
            self.bus = can.interface.Bus(bustype=TODO)
        elif(carModel == GC.ATV and year >= 2022):  #TODO Check years supported
            self.bus = can.interface.Bus(bustype=TODO)
        elif(carModel == GC.ROADSTER_V2 and year >= 2022):  #TODO Check years supported
            self.bus = can.interface.Bus(bustype=TODO)
        elif(carModel == GC.SEMI_TRUCK and year >= 2023):  #TODO Check years supported
            self.bus = canBus.interface.Bus(bustype=TODO)
        else:
            Debug.Lprint("ERROR: This EV's CAN bus is not support by this software. Please buy a Tesla :)")


    def readGasPedalPosition(self, units=GC.PERCENTAGE_UNITS):
    """
    Get the current READ-ONLY position of the accelerator/gas pedal  
    
    Decoder ID's and TODO in Perl
    https://github.com/openvehicles/CAN-RE-Tool/blob/master/rules/teslamodels
    
    Args:
        units: (A string CONSTANT from GlobalConstant.py) Defaults to percentage 
        
    Returns:
        Percentage from 0% to 100% inclusivly OR Distance in mm from 0 to MAX_GAS_PEDAL_TRAVEL 
    """


        # Command to request from CAN bus the current pedal position
        command = TODO [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        
        return canBusPedalSubroutine(GC.GAS_PEDAL, command, units)

    def readGasPedalVelocity(self, units=GC.PERCENTAGE_UNITS):
        
        position1 = readGasPedalPosition(units)
        time.sleep(GC.MIN_CAN_BUS_TIMESTEP)
        position2 = readGasPedalPosition(units)
    
        return (position2 - position1)/GC.MIN_CAN_BUS_TIMESTEP


    def readGasPedalVAcceleration(self, units):
        
        velocity1 = readGasPedalVelocity(units)
        time.sleep(GC.MIN_CAN_BUS_TIMESTEP)
        velocity2 = readGasPedalVelocity(units)
        
        return (velocity2 - velocity1)/GC.MIN_CAN_BUS_TIMESTEP        

    
    def canBusPedalSubroutine(pedalType=GC.GAS_PEDAL, command=GC.GAS_PEDAL_POSITION, units=GC.PERCENTAGE_UNITS):
        msg = canBus.Message(arbitration_id=0x7df, command=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], extended_id=False)
        rawValue = sendMessage(msg)

        if(pedalType == GAS_PEDAL):
            percentOfMax = rawValue/GC.MAX_GAS_PEDAL_TRAVEL
            if(units == GC.PERCENTAGE_UNITS):
                value = percentOfMax
            elif(units == GC.MILLIMETER_UNITS):
                value = percentOfMax * self.CalibratedMaxGasPedalTravel       
            elif(units == GC.CENTIMETER_UNITS):
                value = percentOfMax * (self.CalibratedMaxGasPedalTravel/10)
                
        elif(pedalType == BRAKE_PEDAL):
            percentOfMax = rawValue/GC.MAX_BRAKE_PEDAL_TRAVEL
            if(units == GC.PERCENTAGE_UNITS):
                value = percentOfMax
            elif(units == GC.MILLIMETER_UNITS):
                value = percentOfMax * self.CalibratedMaxBrakePedalTravel       
            elif(units == GC.CENTIMETER_UNITS):
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
    TeslaCanBus.unitTest()
