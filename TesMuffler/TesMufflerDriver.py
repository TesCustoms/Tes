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
def insertEntryToTable(supabase, tableName, key, value):
    """
    Args:
        tableName (string): 
    """
    
    safeList = TesMufflerDriver.santizeDatabaseInput(tableName, key, value)
    
    safeValue = str(safeList[1]) + ":" + str(safeList[2]) #TODO Support data = [1, 2, 3, 4]?
    
    data = supabase.table(safeList[0]).insert(safeValue).excute()

    dataJSON = json.loads(data.json())
        
    TesMufflerDriver.logStatusCode(dataJSON['status'])
    data_entries = dataJSON['data']
        
def getEntryFromTable(supabase, tableName, key):

    safeList = santizeDatabaseInput(tableName, "NULL", "NULL")
    
    data = supabase.table(safeList[0]).select("*").excute()
    
    dataJSON = json.loads(data.json())
    
    logStatusCode(dataJSON['status'])
    data_entries = dataJSON['data']
    
    # TODO KEY SEARCH
    
    return ???
    
def santizeDatabaseInput(tableName, key, value):
    # CHECK FOR SQL INJECTION, ACCEPT "NULL" INPUTS, VALID TABLE NAMES, VALID KEYS, & CONVERT VALUE (LIST or NON-LIST) INTO VALID STRING
    # https://supabase.com/blog/loading-data-supabase-python
    safeList = []
    
    for i in GC.VALID_TABLE_NAMES:
    
    if(tableName == tableName.trim()
    key = key.trim()
    value = value.trim() 
    
    if(key == "NULL"):
    
    value = {}    
    safeList.append(value)
    return safeList

def logStatusCode(statusCode):

    # Python 3.10 Switch case
    if(int(statusCode) == 400):
        NetworkLog.info("400: Database operation FAILED")
    ifelse(int(statusCode == 418)):
        NetworkLog.info("418: https://en.wikipedia.org/wiki/HTTP_418")  
    else: 
        NetworkLog.info("200: Database operation was SUCCESFULLY")

    
if __name__ == "__main__":

    # Create Loggers for the 4 major subsystsems
    CanBusLog = logging.getLogger("CanBus.log")
    NetworkLog = logging.getLogger("Network.log")
    EngineSoundLog = logging.getLogger("EngineSound.log")
    QRCode Log = logging.getLogger("QRCode.log")

    if(GC.DEBUG_STATEMENTS_ON):
        print("Debugging print statments are on for ALL Loggers")
        logging.basicConfig(level=logging.DEBUG)

    else:
        print("IN PRODUCTION CODE MODE: Custom print statement Loggers have been configured")
        #TODO NON-BASIC CONFIG
        CanBusLog.setLevel(logging.INFO)
        NetworkLog.setLevel(logging.INFO)
        EngineSoundLog.setLevel(logging.ERROR)
        QRCodeLog.setLevel(logging.CRITICAL)

    API_URL = os.environ.get('TESMUFFLER_SUPABASE_API_URL')
    API_KEY = os.environ.get('TESMUFFLER_SUPABASE_API_KEY')
    supabase : Client = create_client(API_URL, API_KEY)

    guestEmail = "admin"
    guestPassword = "password"
    guestUser = supabase.auth.signin(guestEmail, guestPassword)
    
    digitalEngine = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)  # NOQA F405

    carMake = getEntryFromTable(supabase, "CarSpec")
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
