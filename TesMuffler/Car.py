#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-04-19"
__doc__     = "Realtime description of a Car objects state including RPM, gear, make, model, year, and color"
"""

try:  # importing internally developed libraries

    # Useful global constants used across all TesMuffler code
    import GlobalConstants as GC

    from TeslaCanBus import *
    # TODO import ApteraCanBus
    # TODO import RivianCanBus
    # TODO import FordCanBus
    # TODO import KiaCanBus

except ImportError:
    print("GlobalConstants.py didn't import correctly")
    print("Please verify that file(s) are in same directory as the Car.py")


class Car:

    def unitTest():
        blazesCar = Car(GC.TESLA, GC.CYBER_TRUCK, 2024, GC.GREY)
        print(blazesCar.color)
        assert blazesCar.currentGear == 1

        elonsCar = Car(GC.TESLA, GC.MODEL_S, 2020, GC.BLUE)
        print(elonsCar.model)
        assert elonsCar.currentRPM == 0
        assert elonsCar.maxRPM == 0

        jeffsCar = Car(GC.FORD, GC.F150_LIGHTNING, 2023, GC.GREEN)
        print(jeffsCar.make)

    def __init__(self, make=GC.TESLA, model=GC.MODEL_S, year=2019, color=GC.WHITE):
        """ TODO

        Code has been tested for 2019 and newer but older Telsa will get support

        Arg(s):
            make = (int, CONSTANT)

        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color

        self.currentGear = 1
        self.currentVelocity = 0
        self.currentRPM = 0
        self.topDigitalGear = GC.TOP_GEAR
        self.maxDigitalRPM = GC.MAX_RPM

        if(make == GC.TESLA):
            self.gearShiftVelocity = [0, 15, 30, 50, 75]
            self.canBus = TeslaCanBus(year, model)          # NOQA F405
        elif(make == GC.APTERA):
            pass
        elif(make == GC.RIVIAN):
            pass
        elif(make == GC.FORD):
            pass
        elif(make == GC.KIA):
            pass
        else:
            pass

    def update(self):
        """_summary_
        """

        # Simialar to OLD bad automatic transmission select gear based on ONLY car velocity on the road (not )
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

    def getGear(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.currentGear


if __name__ == "__main__":
    Car.unitTest()
