#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
"""
# Collect vehicle data to transmit to a central server, hardware switch can turn this off

# Allow program to exit safety and open system files in /sys/class/thermal
# https://docs.python.org/3/library/os.html
import os

import datetime
import uuid


try:  # Importing externally developed libraries

    # Read and Write state of the General Purpose Input / Output pins
    # https://gpiozero.readthedocs.io/en/stable/index.html
    import gpiozero
    #from gpiozero import Button

    # Library for handling data from a car's On-Board Diagnostics port (OBD-II)
    # https://python-obd.readthedocs.io/en/latest/
    import obd

    # Load environment variables for usernames, passwords, & API keys
    # https://pypi.org/project/python-dotenv/
    from dotenv import dotenv_values

    # SQlite connection using turso
    # TODO libsql://tesmuffler-db-opensourceironman.turso.io


except ImportError:
    print("The gpio, obd, dotenv and/or libsql module(s) didn't import correctly!")
    print("Follow the GPIO Zero install instructions at https://gpiozero.readthedocs.io/en/stable/installing.html#")
    print("Follow the python-obd install instructions at https://python-obd.readthedocs.io/en/latest/#installation")
    print("Follow the dotenv install instructions at https://pypi.org/project/python-dotenv/")
    print("Follow the libsql install instructions at https://github.com/tursodatabase/libsql")


## Internally developed modules
# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC

# Realtime description of a vehicle including but not limited to things like RPM, gear, make, model, year, and color
from Vehicle import *


class Telemetrics:

    TURSO_DB_URL = os.environ.get("TURSO_DB_URL")
    TURSO_DB_AUTH_TOKEN = os.environ.get("TURSO_DB_AUTH_TOKEN")


    def unit_test(self):
        """ Test the creation of a Vehicle object and measure the CPU temperature of device running this code

        Arg(s):
            NONE
        """

        BlazeCar = Vehicle(GC.TESLA, GC.CYBER_TRUCK, 2024, GC.GREY, "12345678901234567")
        TestObject1 = Telemetrics(BlazeCar)

        print('Current CPU temperature is {:.2f} degrees Celsius.'.format(Telemetrics.get_cpu_temp()))

        assert TestObject1.isHardwareSecurityEnabled() == False #GC.COLLECTING_DATA
        #TODO assert TestObject1.collect_data_snapshot == [0x00] * GC.SNAPSHOT_SIZE
        #TODO assert TestObject1.send_data_snapshot == GC.DATABASE_OPERATION_SUCCESFULL


    def is_hardware_security_enabled(self):
        """ Read state of GC.SECURITY_TOGGLE_PIN
            https://gpiozero.readthedocs.io/en/stable/recipes.html#button

        Arg(s):
            NONE

        Returns:
            Boolean state of a phyiscal hardware pins inert status
        """
        hardwarePin = gpiozero.Button(GC.SECURITY_TOGGLE_PIN)

        if hardwarePin.is_pressed:  #is_pressed equals is pin pulled LOW is this case
            state = True
        else:
            state = False

        return state


    def get_cpu_temp(self):
        """ Obtains the current CPU temperature in zone #0 in degrees Celsius

        Arg(s):
            NONE

        Returns:
            Current value of the CPU temperature (as float) if successful, zero value otherwise.
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


    def collect_data_snapshot(self):
        """ TODO

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


    def send_data_snapshot(self):
        """ TODO

        """

        data = [0x00] * Telemetrics.SNAPSHOT_SIZE
        if(self.is_hardware_security_enabled() == GC.DATA_COLLECTION_OFF):
            pass # DO NOTHING WITH USER DATA!
        else:
            data = Telemetrics.collect_data_snapshot()

        response = self.SupabaseObject.insertEntryToTable(self.supabaseObject, GC.USER_TABLE, self.VehicleObject.vin, data)   #TODO why two self.SupabaseObject?

        return response


    def __init__(self, VehicleObject):
        """ Telemeteric constructor

	    Args:
	        VehicleObject (Vehicle.py):
        """
        self.VehicleObject = VehicleObject
        self.SupabaseObject = -1 # Client : ????

        # Construct special SQLAlchemy URL to connect to SQlite db on Turso using .env enviroment variables
        config = dotenv_values()
        url = config['TURSO_DB_URL']
        token = config['TURSO_DB_AUTH_TOKEN']
        self.dbUrl = f"sqlite+{url}/?authToken={token}&secure=true"

        current_time = datetime.datetime.now();
        current_time_in_seconds = int(float((current_time-datetime.datetime(1970,1,1)).total_seconds()))
        self.engine = create_engine(self.dbUrl, connect_args={'check_same_thread': False}, echo=True)


if __name__ == "__main__":

        Telemetrics.unit_test()
