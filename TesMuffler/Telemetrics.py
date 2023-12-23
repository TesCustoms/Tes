#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2023-01-13"
__doc__     = "Collect vehicle data to transmit to a central server, hardware switch can turn this off"
"""

# Allow program to exit safety and open system files in /sys/class/thermal
# https://docs.python.org/3/library/os.html
import os

# Allow BASH commands to be run inside Python
# https://docs.python.org/3/library/subprocess.html
from subprocess import check_call

try:  # Importing externally developed libraries

    # Read which Operating System Python code is running on
    # https://docs.python.org/3/library/platform.html
    import platform

    # Read and Write state of the General Purpose Input / Output pins
    # https://gpiozero.readthedocs.io/en/stable/index.html
    from gpiozero import Button

    # Library for handling data from a car's On-Board Diagnostics port (OBD-II)
    # https://python-obd.readthedocs.io/en/latest/
    import obd

    # Open source plaform for NoSQL databases, authentication, file storage, and auto-generated APIs
    # https://github.com/supabase-community/supabase-py
    from supabase import create_client, Client

    # SQlite connection using turso
    # libsql://tesmuffler-db-opensourceironman.turso.io
    # eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIyMDIzLTEyLTE2VDAwOjAxOjM5LjE4NTk4ODc0N1oiLCJpZCI6ImRjMGY1MWU1LTliYTUtMTFlZS1iNTk2LTEyYWIwZGY3MGIxZiJ9.JuKGftAamn3a6-RxA0VnLM1aaEIZIBf78aaAqzUNH0HsZThUzlOCGanHZYwHwQS9EG1tKEoilUuRs36cNa8UCQ


except ImportError:
    print("The gpio, obd, supabase, and/or MySQL module(s) didn't import correctly!")
    executeInstalls = input("Would you like to *** pip3 install obd *** and  *** sudo apt install python3-gpiozero *** (Y/N)? ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        if platform.platform()[0:5] == "PI ARM":  
            check_call("sudo apt install python3-gpiozero", shell=True)
        else:  #Code is running of Windows () or MacOS (Darwin Kernal)
            #MacOS Kernal in called Darwin  
            print(platform.platform)
        check_call("pip install obd", shell=True)
        check_call("pip3 install supabase", shell=True)
        check_call("pip install mysql-connector-python", shell=True)

    else:
        print("You didn't type Y or YES :)")
        print("Follow GPIO Zero manual install instructions at https://gpiozero.readthedocs.io/en/stable/installing.html#")
        print("Follow python-obd manual install instructions at https://python-obd.readthedocs.io/en/latest/#installation")
        print("Follow supabase manual install instructions at https://pypi.org/project/supabase/")
        print("TODO")

# Internally developed modules
# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC

# Realtime description of a Car objects state including RPM, gear, make, model, year, and color
from Vehicle import *


class Telemetrics:

    def unitTest():
        """
        ???
        """

        BlazeCar = Vehicle(GC.TESLA, GC.CYBER_TRUCK, 2024, GC.GREY, "12345678901234567")
        TestObject1 = Telemetrics(BlazeCar)

        print('Current CPU temperature is {:.2f} degrees Celsius.'.format(get_cpu_temp()))

        assert TestObject1.isHardwareSecurityEnabled() == GC.COLLECTING_DATA
        assert TestObject1.collectDataSnapShot == [0x00] * GC.SNAPSHOT_SIZE
        assert TestObject1.sendDataSnapShot == GC.DATABASE_OPERATION_SUCCESFULL

    def is_hardware_security_enabled(self):
        """Read state of GC.SECURITY_TOGGLE_PIN
        https://gpiozero.readthedocs.io/en/stable/recipes.html#button
        """
        toggle = gpiozero.Button(GC.SECURITY_TOGGLE_PIN)
        #GC.SECURITY_TOOGLE_PIN = GPIOX  = X in GC

        if toggle.is_pressed:
            state = True
        else:
            state = False

        return state

    def get_cpu_temp():
        """
        Obtains the current value of the CPU temperature.
        :returns: Current value of the CPU temperature if successful, zero value otherwise.
        :rtype: float
        """
        # Initialize the result.
        result = 0.0
        # The first line in this file holds the CPU temperature as an integer times 1000.
        # Read the first line and remove the newline character at the end of the string.
        if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
            with open('/sys/class/thermal/thermal_zone0/temp') as f:
                line = f.readline().strip()
            # Test if the string is an integer as expected.
            if line.isdigit():
                # Convert the string with the CPU temperature to a float in degrees Celsius.
                result = float(line) / 1000
        # Give the result back to the caller.
        return result

    def collectDataSnapShot():
        """

        """

        data = [0x00] * GC.SNAPSHOT_SIZE
        if(Telemetrics.getHardwareSecurityToggleState == GC.DATA_COLLECTION_OFF):
            pass

        else:
            Obd2Object = obd()
            data[0] = Obd2Object.vin()
            data[1] = Obd2Object.odometerReaing()
            data[2] = Obd2Object.currentSpeed()
            #data[3] = Obd2Object.TODO

        return data

    def sendDataSnapShot(self):
        """
        
        """

        data = [0x00] * Telemetrics.SNAPSHOT_SIZE
        if(self.getHardwareSecurityToggleState == GC.DATA_COLLECTION_OFF):
            pass # DO NOTHING WITH USER DATA!
        else:
            data = Telemetrics.collectDataSnapShot()

        response = self.SupabaseObject.insertEntryToTable(self.supabaseObject, GC.USER_TABLE, self.VehicleObject.vin, data)   #TODO why two    self.SupabaseObject?

        return response

    def __init__(self, VehicleObject):
        """
        
	Args:
	    VehicleObject (Vehicle.py): 
	    SupabaseObject (supabase): 
        """
        self.VehicleObject = VehicleObject
        self.SupabaseObject = -1 # Client : ????


if __name__ == "__main__":

        Telemetrics.unitTest()
