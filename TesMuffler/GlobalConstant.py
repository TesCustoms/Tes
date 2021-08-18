#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-18"
__doc__     = "Useful global constants used across all TesMuffler code"
"""


class GlobalConstant:

    # Vehicle make name CONTSTANTS - Yes these are sorted best to worst :)
    TESLA = 0
    RIVIAN = 1
    FORD = 2
    LUCID = 3
    GMC = 4
    
    # Vehicle model name CONTSTANTS
    MODEL_S = 'S'
    MODEL_3 = '3'
    MODEL_X = 'X'
    MODEL_Y = 'Y'
    CYBER_TRUCK = 'C'
    ATV = 'A'
    ROADSTER_V2 = 'R'
    SEMI_TRUCK = 'S'
    ALL = 'S3XY CARS'

    # Vehicle color CONTSTANTS - ROY G BIV + others
    RED = 0
    ORANGE  = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    INDIGO = 5
    VIOLET = 6
    
    # Moving hardware CONTSTANTS
    GAS_PEDAL = 0                           # Pedal closest to center of the car
    GAS_PEDAL_POSITION = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    DEFAULT_MAX_GAS_PEDAL_TRAVEL = 420      # Units are in millimeters
    MAX_GAS_PEDAL_VALUE = 0x69              # Units are TODO
    BRAKE_PEDAL = 1                         # 2nd pedal from center of thr car
    DEFAULT_MAX_BRAKE_PEDAL_TRAVEL = 69     # Units are in millimeters
    MAX_BRAKE_PEDAL_VALUE = 0xFF            # Units are TODO
    MIN_CAN_BUS_TIMESTEP = 0.001            # Units are seconds
    
    # User Interface CONSTANTS
    UI_TERMINAL_DELAY = 0.1                 # Units are seconds
    MAX_UI_DEALY = 2.0                      # Units are seconds
    FUNCTION_DELAY = 5.0                    # Units are milliSeconds
