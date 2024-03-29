#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-30"
__doc__     = "Realtime description of a Vehicle objects state including RPM, gear, make, model, year, and color"
"""

try:  # Importing externally developed libraries

    pass 

except ImportError:
    print("The obd module didn't import correctly!")
    executeInstalls = input("Would you like to *** pip install obd *** and  *** apt install bluetooth bluez-utils blueman *** for you (Y/N)?  ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("pip install obd", shell=True)
        check_call("sudo apt-get install bluetooth bluez", shell=True) #check_call("sudo apt-get install bluetooth bluez-utils blueman", shell=True)
    else:
        print("You didn't type Y or YES :)")
        print("Follow python-obd manual install instructions at https://python-obd.readthedocs.io/en/latest/#installation")

import TesOBD2

from EngineSoundGenerator import EngineSoundGenerator

# Useful global constants used across all TesMuffler code
import GlobalConstants as GC

    # TODO REMOVE? from TeslaCanBus import *
    # TODO REMOVE? import ApteraCanBus
    # TODO REMOVE? import RivianCanBus
    # TODO REMOVE? import FordCanBus
    # TODO REMOVE? import KiaCanBus


class Vehicle:

    def unitTest():
        blazesCar = Vehicle(GC.TESLA, GC.CYBER_TRUCK, 2024, GC.GREY, "1FALP42X9HF111111")
        print(f"Blaze's truck is a", blazesCar.model)
        assert blazesCar.updatePollingRate == 0.5
        assert blazesCar.currentGear == 1
        assert blazesCar.topDigitalGear == 5
        assert blazesCar.gearShiftVelocity[0] == 0
        assert blazesCar.gearShiftVelocity[GC.TOP_GEAR-1] == 75


        elonsCar = Vehicle(GC.APTERA, GC.MODEL_, 2020, GC.BLUE, "1FTFW1R6XBFB08616")
        print(f"Elon's car is a", elonsCar.model)
        assert elonsCar.currentVelocity == 0
        assert elonsCar.currentRPM == 0
        assert elonsCar.maxDigitalRPM == 10000
        assert elonsCar.vin == "1FTFW1R6XBFB08616"
        assert elonsCar.gearShiftVelocity[elonsCar.topDigitalGear-1] == 80

        jeffsCar = Vehicle(GC.FORD, GC.F150_LIGHTNING, 2023, GC.GREEN, "1G1YY26U0651XXXXX")
        print(f"2023 ==", jeffsCar.year)
        print(f"Jeff's USA truck VIN is", len(jeffsCar.vin), "characters long")
        assert jeffsCar.gearShiftVelocity[0] == 0


    def __init__(self, make=GC.TESLA, model=GC.MODEL_S, year=2022, color=GC.WHITE, vin="12345678901234567", gearShiftVelocity=[0, 15, 30, 50, 75]):
        """Constructor to initialize an Vehicle object

        Defaults to a white 2022 Tesla Model, to make Casey Liss from ATP.fm podcast happy :)

        Code has been tested for 2019 and newer Tesla's, but older Telsa's will get support starting in 2024

        https://en.wikipedia.org/wiki/Vehicle_identification_number

        Arg(s):
            make  (String CONSTANT): Make / Manufacture of a vehicle (Ford, GM, Tesla, & BMW etc)
            model (String CONSTANT): Model from a manufacture that is define by the USA Department of Motor Vehicles (DMV)
            year  (interger): Model year, this is not always the same as the year vehicle was physically built
            color (String CONSTANT): TODO
            vin   (String): Unique Vehicle Identification Number for every vehicle in the USA

        Returns:
           New Vehicle() object
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color

        self.updatePollingRate = GC.STANDARD_POLLING_RATE
        self.currentGear = 1
        self.currentVelocity = 0
        self.currentRPM = 0
        self.topDigitalGear = GC.TOP_GEAR
        self.maxDigitalRPM = GC.MAX_RPM

        self.vin = vin

        self.gearShiftVelocity = [0]
        
        if(make == GC.TESLA):
            self.gearShiftVelocity.append(15)
            self.gearShiftVelocity.append(30)
            self.gearShiftVelocity.append(50)
            self.gearShiftVelocity.append(75)
            self.canBus = TesOBD2.TesOBD2(year, model, make)    # NOQA F405
        elif(make == GC.APTERA):
            self.topDigitalGear = 4                             # Aptera model uses a non-standard 4 gear digital gear box
            self.gearShiftVelocity.append(20)
            self.gearShiftVelocity.append(40)
            self.gearShiftVelocity.append(80)
            self.canBus = TesOBD2.TesOBD2(year, model, make)    # NOQA F405
        elif(make == GC.RIVIAN):
            pass
        elif(make == GC.FORD):
            pass
        elif(make == GC.KIA):
            pass
        else:
            pass

    def update(self):
        """Polling loop to read state of CAN Bus and stare values into Vehicle instance variables at rate of GC.STANDARD_POLLING_RATE

        Arg(s):
            NONE

        Returns:
            NOTHING
        """

        # Simialar to OLD bad automatic transmission select gear based on ONLY vehicle velocity on the road (not RPM or hill angle)
        # TODO Select gear based on road angle and https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching
        if(0 <= self.currentVelocity < self.gearShiftVelocity[1]):
            nextGear = 1
        elif(self.currentVelocity < self.gearShiftVelocity[2]):
            nextGear = 2
        elif(self.currentVelocity < self.gearShiftVelocity[3]):
            nextGear = 3
        elif(self.currentVelocity < self.gearShiftVelocity[4]):
            nextGear = 4
        else:
            nextGear = GC.TOP_GEAR

        # Adjust RPM to a static value based on if downshift or upshift is needed
        if(self.currentGear == nextGear):
            pass
        elif(self.currentGear < nextGear):
            self.currentRPM = 1500
        elif(self.currentGear > nextGear):
            self.currentRPM = 4000

        self.currentGear = nextGear
    def startAudioLoop():
        """_summary_
        """
        
        
    def getGear(self):
        """Get the last gear state (1 to GC.MAX_RPM) stored during update() polling function loop

        Arg(s):
            NONE

        Returns:
            self.currentGear (integer)
        """
        return self.currentGear

    def getRPM(self):
        """Get the last RPM of digital enginer (1 to GC.TOP_GEAR) stored during update() polling function loop

        Arg(s):
            NONE

        Returns:
            self.currentRPM (integer)
        """
        return self.currentRPM

    def getVelocity(self):
        """Get the last velocity stored during update() polling function loop

        Estimate delay from real life velicoty is expected to be 33.3 ms (0.5 Hz)

        Arg(s):
            NONE

        Returns:
            self.currentVelocity (float)
        """
        return self.currentVelocity


if __name__ == "__main__":
    Vehicle.unitTest()
