#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-10"
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

    def __init__(self, device):
        self.logger = "TODO" #obd.logger()

        if(device == GC.MAC):
            self.connection = obd.OBD("/dev/ttyUSB0")
        elif(device == GC.PC):
        elif(device == GC.PI_ZERO_W2 or GC.PI_4):
            HAT_FD
        elif(device == GC.KUKSA_CANOPI):


if __name__ == "__main__":

    UnitTestObject = TesOBD2()
    UnitTestObject.unitTest()
