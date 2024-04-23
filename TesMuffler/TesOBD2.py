#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-14"
__doc__     = "General purpose TesCustoms OBD-2 driver"
"""

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
#TODO REMOVE? from subprocess import Popen, PIPE
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

try:  # Importing externally developed libraries

    # Library for handling data from a car's On-Board Diagnostics port (OBD-II)
    # https://python-obd.readthedocs.io/en/latest/
    import obd

except ImportError:  #TODO
    print("The obd module didn't import correctly!")
    executeInstalls = input("Would you like to *** pip3 install python-obd *** and  *** apt install bluetooth bluez-utils blueman *** for you (Y/N)?  ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("pip install python-obd", shell=False)
        check_call("sudo apt-get install bluetooth bluez-utils blueman", shell=True)
    else:
        print("You didn't type Y or YES :)")
        print("Follow python-obd manual install instructions at https://python-obd.readthedocs.io/en/latest/#installation")

# Import internally developed classes
# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC


class TesOBD2:

    def unitTest(self):
        """ Create basic OBD-2 object, get SPEED, and print value in MPH

        https://python-obd.readthedocs.io/en/latest/#basic-usage
        """
        connection = obd.OBD()

        cmd = obd.commands.SPEED            # Select an OBD command (sensor)

        response = connection.query(cmd)    # Send the command and parse the response

        print(response.value)               # Returns unit-bearing values thanks to Pint

        try:
            print(response.value.to("mph"))     # User-friendly unit conversions

        except AttributeError:
            self.logger.info(f"Reponse to *** {cmd} *** OBD-2 command was not valid")

    def getRpmPint(self):
        """ Get RPM of default wheels, which are the FRONT wheels in a Tesla
        https://python-obd.readthedocs.io/en/latest/Responses/

        Args:
            NONE

        Return:
            OBDResponse (Pint): Python Object containing INT & STRING

        """
        OBDResponseObject = self.connection.query(obd.commands.RPM)   # or obd.commands[1][12] # mode 1, PID 12 (RPM)

        if(OBDResponseObject.is_null()):
            self.logger.debug("OBD-2 command was unable to retrieve data from the vehicle")
        else:
            self.logger.info(f"Raw *** {OBDResponseObject.command} *** command response was *** {OBDResponseObject.message} *** at time = {OBDResponseObject.time} ")
            return OBDResponseObject.value

    def getEngineLoadPint(self):
        """

        https://python-obd.readthedocs.io/en/latest/Responses/
        """
        OBDResponseObject = self.connection.query(obd.commands.ENGINE_LOAD)

        if(OBDResponseObject.is_null()):
            self.logger.debug("OBD-2 command was unable to retrieve data from the vehicle")
        else:
            self.logger.info(f"Raw *** {OBDResponseObject.command} *** command response was *** {OBDResponseObject.message} *** at time = {OBDResponseObject.time} ")
            return OBDResponseObject.value

    def __init__(self, year=GC.TESLA, model=GC.MODEL_3, make=GC.TESLA, loggingLevel="DEBUG"):
        self.logger = obd.logger.setLevel(loggingLevel)  #(obd.logging.loggingLevel) # enables all debug information
        #TODO REMOVE? self.logger = obd.logger()

        try:
            ports = obd.scan_serial()            # Auto scan for available ports to use for CAN Bus
            self.connection = obd.OBD(ports[0], GC.DEFAULT, GC.SAE_J1850PWM, False, GC.MAX_UI_DELAY, True)  #TODO obd.OBD("/dev/ttyUSB0") CHANGE TO GC.FAST   is protocol_id() == 1 or 2 = SAE J1850 PWM or SAE J1850 VPW
            self.logger.info(f"Using *** {ports[0]} *** UNIX device")

        except IndexError:
            self.logger.debug("No UNIX device files available for use as with OBD-2 port / adapter")

        # https://python-obd.readthedocs.io/en/latest/Connections/
        obdStatus = self.connection.status()
        if(obdStatus == OBDStatus.CAR_CONNECTED):
            pass #TODO self.logger.info    (“CAR_CONNECTED”) if the overall connection phase is successful, this status means that the serial communication is valid
        elif(obdStatus == OBDStatus.ELM_CONNECTED):
            pass #TODO self.logger.debug   (“ELM_CONNECTED”) means that the ELM327 processor is reached but the OBDII socket is not connected to the car.
        elif(obdStatus == OBDStatus.OBD_CONNECTED):
            pass #TODO self.logger.debug   (“OBD_CONNECTED”) is returned when the OBDII socket is connected and the ignition is off,
        elif(obdStatus == OBDStatus.NOT_CONNECTED):
            pass #TODO self.logger.info


if __name__ == "__main__":

    UnitTestObject = TesOBD2()
    UnitTestObject.unitTest()

    # ODB-2 commands to use ENGINE_LOAD, RPM, SPEED, DISTANCE_W_MIL, ACCELERATOR_POS_?D?
    # https://python-obd.readthedocs.io/en/latest/Command%20Tables/
    # https://python-obd.readthedocs.io/en/latest/Troubleshooting/
