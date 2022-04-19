#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-04-19"
__doc__     = "High level Car object to enable support Electric Vehicle (EV) companies"
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

    def unitTest():
        blazesCar = Car(GC.TESLA, GC.CYBER_TRUCK, 2024, GC.GREY)
        print(blazesCar.color)

        elonsCar = Car(GC.TESLA, GC.MODEL_S, 2020, GC.BLUE)
        print(elonsCar.model)

        jeffsCar = Car(GC.FORD, GC.F150_LIGHTNING, 2023, GC.GREEN)
        print(jeffsCar.make)


    def __init__(self, make=GC.TESLA, model=GC.MODEL_S, year=2019, color=GC.RED):
        """Code has been tested for 2019 and newer but older Telsa will get support
        
        Arg(s):
        make = (int, CONSTANT) 

        """ 
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        

if __name__ == "__main__":
    Car.unitTest()
