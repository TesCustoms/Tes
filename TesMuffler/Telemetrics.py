#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-11-02"
__doc__     = "Collect vehicle data to transmit to a central server, hardware switch can turn this off"
"""

try:  # Importing externally developed libraries

    from gpiozero import Button

    import obd

    # Open source plaform for NoSQL databases, authentication, file storage, and auto-generated APIs
    # https://github.com/supabase-community/supabase-py
    from supabase import create_client, Client

    # MySQL
    import mysql-connector-python

except ImportError:  #TODO
    print("The obd module didn't import correctly!")
    executeInstalls = input("Would you like to *** pip3 install python-obd *** and  *** sudo apt install python3-gpiozero *** (Y/N)? ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("pip install python-obd", shell=False)
        check_call("sudo apt-get install bluetooth bluez-utils blueman", shell=True)
        check_call("sudo apt install python3-gpiozero", shell=True)
        check_call("pip install mysql-connector-python", shell=True)

    else:
        print("You didn't type Y or YES :)")
        print("Follow python-obd manual install instructions at https://python-obd.readthedocs.io/en/latest/#installation")
        print("Follow GPIO Zero manual install instructions at https://gpiozero.readthedocs.io/en/stable/installing.html#")

# Internally developed modules
# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC

# Realtime description of a Car objects state including RPM, gear, make, model, year, and color
from Vehicle import *


class Telemetrics:

    SNAPSHOT_SIZE = 3

    def unitTest():
        """
        
        """

        BlazeCar = Car(GC.TESLA, GC.CYBER_TRUCK, 2024, GC.GREY)
        TestObject1 = Telemetrics(BlazeCar)
        assert TestObject1.getHardwareSecurityToggleState == GC.DATA_COLLECTION_OFF  # GC.DATA_COLLECTION_OFF = 0 in GC

        assert TestObject1.collectDataSnapShot == [0x00] * GC.SNAPSHOT_SIZE

        assert TestObject1.sendDataSnapShot == GC.DATABASE_OPERATION_SUCCESFULL

    def getHardwareSecurityToggleState(self):
        """
        https://gpiozero.readthedocs.io/en/stable/recipes.html#button
        """
        toggle = Button(GC.SECURITY_TOOGLE_PIN)    #GC.SECURITY_TOOGLE_PIN = GPIOX  = X in GC

        if toggle.is_pressed:
            state = True
        else:
            state = False

        return state

    def collectDataSnapShot():
        """

        """

        data = [0x00] * Telemetrics.SNAPSHOT_SIZE
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
