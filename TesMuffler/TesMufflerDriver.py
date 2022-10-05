#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-01"
__doc__     = "TesMuffler project code starts running here"
"""

# Allow CLI to pass parameters into this driver for testing
# https://docs.python.org/3/library/argparse.html
import argparse

# Allow program to exit safety and use enviroment variables for passwords and API keys
# https://docs.python.org/3/library/os.html
import os
import sys

# Open source plaform for NoSQL databases, authentication, file storage, and auto-generated APIs
# https://github.com/supabase-community/supabase-py
from supabase import create_client, Client

try:  # importing internally developed libraries
    # Create pitch varying audio of a library of cars in real-time on low processing power CPUs
    from EngineSoundGenerator import *

    # Realtime description of a Car objects state including RPM, gear, make, model, year, and color
    from Car import *

    # Useful global constants for the entire TesCustoms TesMuffler library
    import GlobalConstants as GC

except ImportError:  #TODO
    print("EngineSoundGenerator.py, car.py, OR  GlobalConstants.py didn't import correctly")
    print("Please verify that those files are in same directory as the TesMufflerDriver.py")

# Flexible event logging system for DEBUGGING, ERRORS, and INFO
# https://docs.python.org/3/library/logging.html
import logging


# https://supabase.com/blog/loading-data-supabase-python#more-python-and-supabase-resources
def addEntryTable(supabase, tableName, value):
    
    data = supabase.table(tableName).insert(value).excute()


def getEntryFromTable(supabase, tableName, key):

if __name__ == "__main__":

    # Create Loggers for the 4 major subsystsems
    CanBusLog = logging.getLogger("CanBus.log")
    WirelessLog = logging.getLogger("Wireless.log")
    EngineSoundLog = logging.getLogger("EngineSound.log")
    QRCodeLog = logging.getLogger("QRCode.log")

    if(GC.DEBUG_STATEMENTS_ON):
        print("Debugging print statments are on for ALL Loggers")
        logging.basicConfig(level=logging.DEBUG)

    else:
        print("IN PRODUCTION CODE MODE: Custom print statement Loggers have been configured")
        #TODO NON-BASIC CONFIG
        CanBusLog.setLevel(logging.INFO)
        WirelessLog.setLevel(logging.INFO)
        EngineSoundLog.setLevel(logging.ERROR)
        QRCodeLog.setLevel(logging.CRITICAL)

    API_URL = os.environ.get('TESMUFFLER_SUPABASE_API_URL')
    API_KEY = os.environ.get('TESMUFFLER_SUPABASE_API_KEY')
    supabase = create_client(API_URL, API_KEY)

    guestEmail = "admin"
    guestPassword = "password"
    guestUser = supabase.auth.signup(guestEmail, guestPassword)
    
    digitalEngine = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)  # NOQA F405

    carMake = GC.TESLA       #TODO = supabase.__getattribute__(make)
    carModel = GC.MODEL_3    #TODO = supabase.__getattribute__(model)
    carYear = 2022           #TODO = supabase.__getattribute__(year)
    carColor = GC.WHITE      #TODO = supabase.__getattribute__(color)
    digitalCar = Car(carMake, carModel, carYear, carColor)

    while(True):
        #TODO if supabase.__getattribute__(changeBit)
        
        try:
            digitalCar.update()
            digitalEngine.startAudioLoop()

        except KeyboardInterrupt:
            print(f"\nEXITTING PROGRAM")
            sys.exit(0)

        # TODO
        #except ProgramCrash:
        #    print(f"\nEXITTING PROGRAM")
        #    check_call("python3 TesMufflerDriver.py", shell=True)
