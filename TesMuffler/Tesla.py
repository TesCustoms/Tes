#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-17"
__doc__     = "Simulated Tesla vehicle"
"""

# Internally developed mocules

# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC

# Realtime description of a Vehicle objects state including RPM, gear, make, model, year, and color
from Vehicle import *

class Tesla:

    def unitTest(self):
        pass

    def __init__(self):
        self.VehicleObject = Vehicle()  # NOQA F405


if __name__ == "__main__":

    TeslaModel3 = Tesla(GC.TeslaModel3)
    TeslaModel3.unitTest()
