#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-09"
__doc__     = "Collect vehicle data to transmit to a central server, hardware switch can turn this off"
"""

try:  # Importing externally developed libraries
    
    from gpiozero import Button
    
    import obd

    # Open source plaform for NoSQL databases, authentication, file storage, and auto-generated APIs
    # https://github.com/supabase-community/supabase-py
    from supabase import create_client, Client 

except ImportError:  #TODO
    print("Either gpiozero, python-obd or supabaase didn't import correctly")
    print("Please verify that you pip3 installed both modules")


# Internally developed mocules 

# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC

# Realtime description of a Car objects state including RPM, gear, make, model, year, and color
from Car import *


class Telemetrics:


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

        data = [0x00] * GC.SNAPSHOT_SIZE
        if(Telemetrics.getHardwareSecurityToggleState == GC.DATA_COLLECTION_OFF):
            pass

        else:
            Obd2Object = obd()
            data[0] = Obd2Object.odometerReaing()
            data[1] = Obd2Object.currentSpeed()
            data = [0x69]   #TODO


        return data

    def sendDataSnapShot(self):
        """
        
        """

        data = [0x00] * GC.SNAPSHOT_SIZE
        if(self.getHardwareSecurityToggleState == GC.DATA_COLLECTION_OFF):
            exit 

        else:
            data = Telemetrics.collectDataSnapShot()
            
        self.SupabaseObject.insertEntryToTable(self.supabaseObject, GC.USER_TABLE, self.CarObject.vin, data)   #TODO why two    self.SupabaseObject?


    def __init__(self, CarObject, SupabaseObject):
        """
        
        """
        self.CarObject = CarObject
        self.SupabaseObject = SupabaseObject


if __name__ == "__main__":

        Telemetrics.unitTest()
