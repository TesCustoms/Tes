#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-07-21"
__doc__     = "Useful global constants used across all TesMuffler code base"
"""

# Vehicle make name CONTSTANTS - Yes these are sorted best to worst :)
TESLA = 0
APTERA = 1
RIVIAN = 2
FORD = 3
KIA = 4

# Vehicle model name CONTSTANTS for vehicle makes above
MODEL_S = 'S'
MODEL_3 = '3'
MODEL_X = 'X'
MODEL_Y = 'Y'
CYBER_TRUCK = 'C'
ATV = 'A'
ROADSTER_V2 = 'R'
SEMI_TRUCK = 'S'
ALL_TESLAS = 'S3XY CARS'

SURYA = 'SURYA'  # TODO once model name is public

RT1 = 'RT1' 
RS1 = 'RS1'

F150_LIGHTNING = 'F-150L'
MACH_E = 'MACH-E'

EV6 = 'EV6'

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
MAX_GAS_PEDAL_TRAVEL = TOD)     # Units are in millimeters

BRAKE_PEDAL = 1                 # 2nd pedal from center of the car
BRAKE_PEDAL_POSITION = [TODO, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
MAX_BRAKE_PEDAL_TRAVEL = 69     # Units are in millimeters

MIN_CAN_BUS_TIMESTEP = 0.001    # Units are Seconds
    
# User Interface CONSTANTS
UI_TERMINAL_DELAY = 0.1         # Units are seconds
MAX_UI_DEALY = 2.0              # Units are seconds
FUNCTION_DELAY = 5.0            # Units are milliseconds

# Integer unit CONSTANTS
PERCENTAGE_UNITS = '%'
MILLIMETER_UNITS = 'mm'


class GlobalConstant:

    def unitTest():
        assert UI_TERMINAL_DELAY < 0.5
        
        assert MAX_GAS_PEDAL_TRAVEL == 0xFF
        assert MAX_BRAKE_PEDAL_TRAVEL < 256

        command = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        assert command == GAS_PEDAL_POSITION

        assert RED == 0
        
        assert MODEL_S == 'S'
        assert MODEL_S == "S" 

        assert TESLA != FORD
       
        assert MODEL_S == '3', "Unit Test failed successfully"


if __name__ == "__main__":
    print("Starting GlobalConstant.py unitTest() for TesMuffler library")
    GlobalConstant.unitTest()
