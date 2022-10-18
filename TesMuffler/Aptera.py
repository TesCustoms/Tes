#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-18"
__doc__     = "Simulated Aptera vehicle"
"""

# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

# Internally developed modules

# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC

# Realtime description of a Vehicle objects state including RPM, gear, make, model, year, and color
from Vehicle import *


class Aptera:

    def unitTest(self):
        assert  self.VehicleObject.getGear() == 1
        assert  self.VehicleObject.getVelocity() == 0
        assert  self.VehicleObject.getRPM() == 0

        for time in range(100):
            print("Polling current RPM, velocity, and gear from CAN Bus at 1 Hz")
            self.VehicleObject.update()
            time.sleep(1)

            print(f"Current gear is {self.VehicleObject.getGear()}")
            print(f"Current velocity is {self.VehicleObject.getVelocity()}")
            print(f"Current RPM is {self.VehicleObject.getRPM()}")


    def __init__(self):
        self.VehicleObject = Vehicle(GC.APTERA, GC.MODEL_, 2023)  	# NOQA F405


if __name__ == "__main__":

    productionCar = Aptera()
    productionCar.unitTest()
