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

class TeslaCanBus:

    FAST = 1000000  # 1 Mbit/sec (Mbps)
    SLOW = 20000    # 20 kbits/sec (kbps)
    
    def unitTest():
    
    
    def __init__(self, channel=0, bitrate=FAST):
        self.bus = can.interface.Bus(bustype=)
        
    def readGasPedalPosition():


    def readGasPedalVelocity():

    def readGasPedalVAcceleration():

if __name__ == "__main__":
    
    unitTest()
    