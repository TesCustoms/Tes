#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-09-30"
__doc__     = "TesMuffler project code starts running here"
"""

# Allow CLI to pass parameters into this driver for testing
# https://docs.python.org/3/library/argparse.html
import argparse

# Allow program use enviroment variables and determine filename of current file
# https://docs.python.org/3/library/os.html
import os

import sys

# Allow data from iOS and Android Supabase database to be accessed via API
# https://docs.python.org/3/library/json.html
import json

# Open source NoSQL databased
# https://github.com/supabase-community/supabase-py
from supabase import create_client

# Play custom engine sounds
# http://www.mega-nerd.com/SRC/
from EngineSoundGenerator import *

# Global constants of TesCustoms TesMuffler library
import GlobalConstants as GC


# Flexible event logging system for DEBUGGING, ERRORS, and INFO 
# https://docs.python.org/3/library/logging.html
import logging


if __name__ == "__main__":

    # Create Loggers for the 4 major subsystsems
    CanBusLog = logging.Logger("CanBus.log")
    WirelessLog = logging.Logger("Wireless.log")
    EngineSoundLog = logging.Logger("EngineSound.log")
    QRCodeLog = logging.Logger("QRCode.log")

    if(GC.DEBUG_STATEMENTS_ON):
        print("Debugging print statments are on for CanBus, Bluetooth, EngineeSound, and QR Code Loggers")
        CanBusLog.setLevel(logging.DEBUG)
        WirelessLog.setLevel(logging.DEBUG)
        EngineSoundLog.setLevel(logging.DEBUG)
        QRCodeLog.setLevel(logging.DEBUG)

    else:
        print("Custom user info print statement Loggers have been configured for PRODUCTION code")
        CanBusLog.setLevel(logging.INFO)
        WirelessLog.setLevel(logging.INFO)
        EngineSoundLog.setLevel(logging.ERROR)
        QRCodeLog.setLevel(logging.CRITICAL)

    TES_API_URL = os.environ.get('TES_API_URL')
    TES_API_KEY = os.environ.get('TES_API_KEY')
    supabase = create_client(TES_API_URL, TES_API_KEY)

    digitalEngine = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1, EngineSoundLog)

    while(True):

        try:
            digitalEngine.startAudioLoop()

        except KeyboardInterrupt:
            print(f"\nEXITTING PROGRAM")
            sys.exit(0)
