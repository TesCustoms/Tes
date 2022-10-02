#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-01"
__doc__     = "Useful global constants for the entire TesCustoms TesMuffler library"
"""
TODO = -1

DEBUG_STATEMENTS_ON = True

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

R1T = 'R1T'
R1S = 'R1S'

F150_LIGHTNING = 'F-150L'
MACH_E = 'MACH-E'

EV6 = 'EV6'

# Vehicle color CONTSTANTS - ROY G BIV + others
RED = 0
ORANGE = 1
YELLOW = 2
GREEN = 3
BLUE = 4
INDIGO = 5
VIOLET = 6
GREY = 7
WHITE = 8

# Moving hardware CONTSTANTS
GO_PEDAL = 0                    # Pedal furthest right
GO_PEDAL_POSITION_ID = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
MAX_GO_PEDAL_TRAVEL = TODO      # Units are in millimeters
TOP_GEAR = 5
MAX_RPM = 10_000

BRAKE_PEDAL = 1                 # 2nd pedal from center of the car
BRAKE_PEDAL_POSITION_ID = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]  # TODO
MAX_BRAKE_PEDAL_TRAVEL = 69     # Units are in millimeters

# User Interface CONSTANTS
UI_TERMINAL_DELAY = 0.1         # Units are seconds
MAX_UI_DEALY = 2.0              # Units are seconds
FUNCTION_DELAY = 0.005          # Units are seconds
MIN_CAN_BUS_TIMESTEP = 0.001    # Units are seconds

# Dimensional unit CONSTANTS
PERCENTAGE_UNITS = '%'
MILLIMETER_UNITS = 'mm'
CENTIMETER_UNITS = 'cm'


class GlobalConstants:

    def unitTest():
        assert UI_TERMINAL_DELAY < 0.5

        assert MAX_GO_PEDAL_TRAVEL == TODO
        assert MAX_BRAKE_PEDAL_TRAVEL < 256

        command = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        assert command == GO_PEDAL_POSITION_ID

        assert RED == 0

        assert MODEL_S == 'S'
        assert MODEL_S == "S"

        assert TESLA != FORD

        assert MODEL_S == '3', "Unit Test failed successfully"
    
if __name__ == "__main__":
    print("Starting GlobalConstants.py unitTest() for TesMuffler library")
    GlobalConstants.unitTest()
