#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-18"
__doc__     = "High level Car object to enable support all Electric Vehicle (EV) companies"
"""

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# Access internally developed libraries
try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    import Debug

    # Useful global constants used across all TesMuffler code
    import GlobalConstant as GC

except ImportError:
    print("Debug.py or GlobalConstant.py didn't import correctly")
    print("Please verify that those files are in same directory as the TeslaCanBus.py")
    #TODO

class Car:

    def __init__(make=GC.TESLA, model=GC.MODEL_S, year=2019, color=GS.RED):
        """Code has been tested for 2019 and newer but older Telsa will get support
        """ 
        self.make = 
        self.model = 
        self.year = 
        self.color = 
        