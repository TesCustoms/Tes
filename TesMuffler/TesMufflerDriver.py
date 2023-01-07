#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2023-01-06"
__doc__     = "TesMuffler embedded linux backend code starts running here"
"""

# Allow CLI to pass parameters into this driver for testing
# https://docs.python.org/3/library/argparse.html
import argparse

# Python interactive source code debugger to set breakpoints
# https://docs.python.org/3/library/pdb.html
import pdb

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
    from supabase import create_client, Client   #TODO REMOVE?, execute

except ImportError:
    print("ERROR: The supabase python module didn't import correctly!")
    executeInstalls = input("Would you like me to *** pip3 install supabase *** for you (Y/N)? ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("sudo apt install python3-pip", shell=True)
        check_call("pip3 install supabase", shell=True)
    else:
        print("You didn't type Y or YES :)")
        print("Follow supabase manual install instructions at https://pypi.org/project/supabase/")

# Realtime description of a Vehicle objects state including RPM, gear, make, model, year, and color
from Vehicle import Vehicle

# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC


def insertValueIntoTable(supabase, tableName, key, value):
    """Insert value object into unique key in NoSQL table called "tableName"

    https://hazelcast.com/glossary/key-value-store/
    https://supabase.com/blog/loading-data-supabase-python
    https://supabase.com/blog/loading-data-supabase-python#more-python-and-supabase-resources

    Arg(s):
        tableName (String): See GC.VALID_SUPABASE_TABLE_NAMES for valid table names
        key (String): Unique search key to index data on TODO
        value (String): Arbitrary large data field to insert into TODO ???END?? of table

    Returns:
        HTTP Status Code of database API call
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

    data = supabase.table(safeList[0]).select("*").execute()

    # Select a single row from the 'users' table
    #result = supabase.execute('SELECT * FROM users WHERE id = $1', (1,))
    #print(result['rows'][0])


    dataJSON = json.loads(data.json())

    statusCode = logStatusCode(dataJSON['status'])
    data_entries = dataJSON['data']

    # TODO KEY SEARCH

    return statusCode


def santizeDatabaseInput(tableName, key, value):
    # CHECK FOR SQL INJECTION, ACCEPT "NULL" INPUTS, VALID TABLE NAMES, VALID KEYS, & CONVERT VALUE (LIST or NON-LIST) INTO VALID STRING
    # https://supabase.com/blog/loading-data-supabase-python
    safeList = []

    for i in range(len(GC.VALID_SUPABASE_TABLE_NAMES)):
        if(GC.VALID_SUPABASE_TABLE_NAMES[i] == tableName.strip()):
            key = key.strip()
            value = value.strip()

        if(key == "NULL"):
            value = {}
            safeList.append(value)

    return safeList


def logStatusCode(statusCode):

    # Python 3.10 Switch case
    if(int(statusCode) == GC.DATABASE_OPERATION_FAILED):
        NetworkLog.info("400: Database operation FAILED")
    elif(int(statusCode == 418)):
        NetworkLog.info("418: https://en.wikipedia.org/wiki/HTTP_418")
    elif(int(statusCode == GC.DATABASE_OPERATION_SUCCESFULL)):
        NetworkLog.info("200: Database operation was SUCCESFULLY")
    else:
        NetworkLog.info("TODO: Unknown HTTP ERROR CODE!")

    return statusCode


if __name__ == "__main__":

    # Create a command line parser
    parser = argparse.ArgumentParser(prog="TesMuffler v2022.0", description=__doc__, add_help=True)
    parser.add_argument("-d", "--DebugPrintStatementsOn", type=int, default=0, help="Global print() statement toggle for entire TesMuffler library")  # NOQA E501
    #TODO parser.add_argument("-u", "--unit", type=str, default=FIELD_MODE, choices=[TESTING_MODE, FIELD_MODE, PRODUCT_MODE], help="Select boot up mode for BARISTO kiosk.")
    args = parser.parse_args()

    # Create Loggers for the 4 major subsystsems
    CanBusLog = logging.getLogger("CanBus.log")
    NetworkLog = logging.getLogger("Network.log")
    EngineSoundLog = logging.getLogger("EngineSound.log")
    QRCodeLog = logging.getLogger("QRCode.log")

    # Make LOCAL non-git version controlled enviroment variables are set for supabase API URL &  KEY
    #TODO check_call("source .bashrc", shell=False)

    if(GC.DEBUG_STATEMENTS_ON or args.DebugPrintStatementsOn):
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
    supabase: Client = create_client(API_URL, API_KEY)

    guestEmail = "info@tescustoms.com"
    guestPassword = "password"
    guestUser = supabase.auth.sign_up(email=guestEmail, password=guestPassword)
    guestUser = supabase.auth.sign_in(email=guestEmail, password=guestPassword)

    #TODO move to Vehicle.py digitalEngine = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)  # NOQA F405

    # Initial default Vehicle on first app and backend run with user VIN 
    digitalVehicle = Vehicle(vin=getEntryFromTable(supabase, GC.VALID_SUPABASE_TABLE_NAMES[0], "vin"))
    statusCode = insertValueIntoTable(supabase, GC.VALID_SUPABASE_TABLE_NAMES[1], vin, digitalVehicle)

    digitalVehicle.startAudioLoop()
    while(True):
        #TODO if supabase.__getattribute__(changeBit)

        try:
            digitalVehicle.update()
            digitalVehicle.startAudioLoop()

        except KeyboardInterrupt:
            print(f"\nEXITTING PROGRAM")
            sys.exit(0)

        # TODO
        #except ProgramCrash:
        #    print(f"\nEXITTING PROGRAM")
        #    check_call("python3 TesMufflerDriver.py", shell=True)
