#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-13"
__doc__     = "Read only class for the OBD-II Tesla CAN Bus"
"""

# Interface with Tesla ODB via CAN Bus
# https://python-can.readthedocs.io/en/2.1.0/index.html#
import can

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

try:
    # Generate .txt data logging and custom terminal debugging output
    from Debug import *
    #TODO

except ImportError:
	print("Debug didn't import correctly, please verify that Debug.py is in TODO")
	#TODO


class TeslaCanBus:

	#Debugging CONSTANTS
	DEBUG_STATEMENTS_ON = True

    FAST = 1000000  # 1 Mbit/sec (Mbps)
    SLOW = 20000    # 20 kbits/sec (kbps)
    
    def unitTest():
    
    
    def __init__(self, channel=0, bitrate=TeslaCanBus.FAST):

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(TeslaCanBus.DEBUG_STATEMENTS_ON, thisCodesFilename)
        
        self.bus = can.interface.Bus(bustype=)
        
    def readGasPedalPosition():
        data = TODO
        msg = can.Message(arbitration_id=0x7df, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], extended_id=False)
        sendMessage(msg)

    def readGasPedalVelocity():
        #TODO COPY readGasPedalPosition()

    def readGasPedalVAcceleration():
        #TODO COPY readGasPedalPosition()

    def sendMessage(self, msg):
        try:
            bus.send(msg)
            print("CAN Bus message sent on {}".format(bus.channel_info))
        except can.CanError:
            print("CAN Bus message was NOT sent")            


if __name__ == "__main__":
    
    unitTest()
    