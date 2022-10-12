#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-11"
__doc__     = "General purpose TesCustoms OBD-2 driver"
"""

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
#TODO REMOVE? from subprocess import Popen, PIPE
from subprocess import check_call

try:  # Importing externally developed libraries

    # Library for handling data from a car's On-Board Diagnostics port (OBD-II)
    # https://python-obd.readthedocs.io/en/latest/
    import obd

except ImportError:  #TODO
    print("The python-obd module didn't import correctly!")
    executeInstalls = input("Would you like to *** pip3 install python-obd *** and  *** apt install bluetooth bluez-utils blueman *** for you (Y/N)?")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("pip3 install python-obd", shell=True)
        check_call("sudo apt-get install bluetooth bluez-utils blueman", shell=True)
    else:
        print("You didn't type Y or YES :)")
        print("Follow python-obd manual install instructions at https://python-obd.readthedocs.io/en/latest/#installation")

# Import internally developed classes
# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC


class TesOBD2:

    def unitTest(self):
        connection = obd.OBD()

        cmd = obd.commands.SPEED            # Select an OBD command (sensor)

        response = connection.query(cmd)    # Send the command and parse the response

        print(response.value)               # Returns unit-bearing values thanks to Pint

        try:
            print(response.value.to("mph"))     # User-friendly unit conversions

        except AttributeError:
            print(f"Reponse to *** {cmd} *** OBD-2 command was not valid")
            #self.logger.info(f"Reponse to *** {cmd} *** OBD-2 command was not valid")

        print(GC.CENTIMETER_UNITS)

    def getRPM(self):
        """
        """
        OBDResponseObject = self.connection.query(obd.commands.RPM, )

        if(OBDResponseObject.is_null()):
            pass #TODO self.logger.debug("OBD-2 command was unable to retrieve data from the vehicle")


    def __init__(self, year=GC.TESLA, model=GC.MODEL_3, make=GC.TESLA):
        self.logger = "TODO" #obd.logger()

        try:
            ports = obd.scan_serial()            # Auto scan for available ports to use for CAN Bus 
            self.connection = obd.OBD(ports[0], GC.DEFAULT,TODO, False, GC.MAX_UI_DELAY, True)  #TODO obd.OBD("/dev/ttyUSB0") CHANGE TO GC.FAST
            pass #TODO self.logger.info(f"Using *** {ports[0]} *** UNIX device")

        except IndexError:
            pass #TODO self.logger.debug("No UNIX device files available for use as with OBD-2 port / adapter")

        # https://python-obd.readthedocs.io/en/latest/Connections/
        obdStatus = self.connection.status()
        if(obdStatus == OBDStatus.CAR_CONNECTED):
            pass #TODO self.logger.info
        elif(obdStatus == OBDStatus.ELM_CONNECTED):
            pass #TODO self.logger.debug
        elif(obdStatus == OBDStatus.OBD_CONNECTED):
            pass #TODO self.logger.debug
        elif(obdStatus == OBDStatus.NOT_CONNECTED):
            pass #TODO self.logger.info


if __name__ == "__main__":

    UnitTestObject = TesOBD2()
    UnitTestObject.unitTest()

    # ODB-2 commands to use ENGINE_LOAD, RPM, SPEED, DISTANCE_W_MIL, ACCELERATOR_POS_?D?
    # https://python-obd.readthedocs.io/en/latest/Command%20Tables/
