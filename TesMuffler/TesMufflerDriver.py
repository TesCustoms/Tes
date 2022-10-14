#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-14"
__doc__     = "TesMuffler embedded linux code starts running here"
"""

# Allow CLI to pass parameters into this driver for testing
# https://docs.python.org/3/library/argparse.html
import argparse

# Allow program to exit safety and use enviroment variables for passwords and API keys
# https://docs.python.org/3/library/os.html
import os
import sys

# Allow decoding of supabase database responses
# https://docs.python.org/3/library/json.html
import json

# Flexible event logging system for DEBUGGING, ERRORS, and INFO
# https://docs.python.org/3/library/logging.html
import logging

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
#TODO REMOVE? from subprocess import Popen, PIPE
from subprocess import check_call

try:  # Importing externally developed libraries

    # Open source plaform for NoSQL databases, authentication, file storage, and auto-generated APIs
    # https://github.com/supabase-community/supabase-py
    from supabase import create_client, Client

except ImportError:  #TODO
    print("ERROR: The supabase python module didn't import correctly!")
    executeInstalls = input("Would you like me to *** pip3 install supabase *** for you (Y/N)? ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("pip3 install supabase", shell=True)
    else:
        print("You didn't type Y or YES :)")
        print("Follow supabase manual install instructions at https://pypi.org/project/supabase/")

# Create pitch varying audio of a library of vahicles in real-time on low processing power CPUs
from EngineSoundGenerator import *

# Realtime description of a Vehicle objects state including RPM, gear, make, model, year, and color
from Vehicle import *

# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC

# https://supabase.com/blog/loading-data-supabase-python#more-python-and-supabase-resources
def insertEntryToTable(supabase, tableName, key, value):
    """
    Args:
        tableName (string): 
        key (string):
        value (string): 
    """

    safeList = santizeDatabaseInput(tableName, key, value)

    safeValue = str(safeList[1]) + ":" + str(safeList[2]) #TODO Support data = [1, 2, 3, 4]?

    data = supabase.table(safeList[0]).insert(safeValue).excute()

    dataJSON = json.loads(data.json())

    statusCode = logStatusCode(dataJSON['status'])
    data_entries = dataJSON['data']

    return statusCode

def getEntryFromTable(supabase, tableName, key):

    safeList = santizeDatabaseInput(tableName, "NULL", "NULL")

    data = supabase.table(safeList[0]).select("*").excute()

    dataJSON = json.loads(data.json())

    statusCode = logStatusCode(dataJSON['status'])
    data_entries = dataJSON['data']

    # TODO KEY SEARCH

    return statusCode

def santizeDatabaseInput(tableName, key, value):
    # CHECK FOR SQL INJECTION, ACCEPT "NULL" INPUTS, VALID TABLE NAMES, VALID KEYS, & CONVERT VALUE (LIST or NON-LIST) INTO VALID STRING
    # https://supabase.com/blog/loading-data-supabase-python
    safeList = []

    for i in GC.VALID_TABLE_NAMES:
        if(VALID_TABLE_NAMES[i] == tableName.trim()):
            key = key.trim()
            value = value.trim()

        if(key == "NULL"):
            value = {}
            safeList.append(value)

    return safeList

def logStatusCode(statusCode):
    #TODO GC.DATABASE_OPERATION_FAILED = 400, GC.DATABASE_OPERATION_SUCCESFULL = 200

    # Python 3.10 Switch case
    if(int(statusCode) == 400):
        NetworkLog.info("400: Database operation FAILED")
    elif(int(statusCode == 418)):
        NetworkLog.info("418: https://en.wikipedia.org/wiki/HTTP_418")
    else: 
        NetworkLog.info("200: Database operation was SUCCESFULLY")

    return statusCode


if __name__ == "__main__":

    # Create Loggers for the 4 major subsystsems
    CanBusLog = logging.getLogger("CanBus.log")
    NetworkLog = logging.getLogger("Network.log")
    EngineSoundLog = logging.getLogger("EngineSound.log")
    QRCodeLog = logging.getLogger("QRCode.log")

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

    vehicleMake = getEntryFromTable(supabase, "VehicleSpec")
    vehicleModel = GC.MODEL_3    #TODO = supabase.__getattribute__(model)
    vehicleYear = 2022           #TODO = supabase.__getattribute__(year)
    vehicleColor = GC.WHITE      #TODO = supabase.__getattribute__(color)
    digitalVehicle = Vehicle(vehicleMake, vehicleModel, vehicleYear, vehicleColor)

    while(True):
        #TODO if supabase.__getattribute__(changeBit)

        try:
            digitalvehicle.update()
            digitalEngine.startAudioLoop()

        except KeyboardInterrupt:
            print(f"\nEXITTING PROGRAM")
            sys.exit(0)

        # TODO
        #except ProgramCrash:
        #    print(f"\nEXITTING PROGRAM")
        #    check_call("python3 TesMufflerDriver.py", shell=True)
