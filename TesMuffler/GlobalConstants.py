#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-10"
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

F150_LIGHTNING = 'F-150 LIGHTNING'
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
GO_PEDAL = 0                    # Pedal furthest right in the UK and USA
GO_PEDAL_POSITION_CAN_BUS_IDENTIFIER = [0b11_111_111_111]    #TODO or 29bit?
MAX_GO_PEDAL_TRAVEL = TODO      # Units are in millimeters

BRAKE_PEDAL = 1                 # Pedal furthest left in automatic transmissions in UK and USA
BRAKE_PEDAL_POSITION_CAN_BUS_IDENTIFIER = [0b11_111_111_111]    #TODO or 29bit?
MAX_BRAKE_PEDAL_TRAVEL = TODO     # Units are in millimeters

# Digital simulation of hardware CONSTANTS
TOP_GEAR = 5
MAX_RPM = 10_000

# Tesla API CONSTANTS
VELOCITY_SENSOR_CAN_BUS_IDENTIFIER = [0b11_111_111_111]    #TODO or 29bit?
ENGINE_LOAD_CAN_BUS_IDENTIFIER = [0b11_111_111_111]    #TODO or 29bit?
RPM_CAN_BUS_IDENTIFIER = [0b11_111_111_111]    #TODO or 29bit?

ODDOMETER_CAN_BUS_IDENTIFIER = [0b11_111_111_111]    #TODO or 29bit?
HYBRID_BATTERY_REMAINING_CAN_BUS_IDENTIFIER = [0b11_111_111_111]    #TODO or 29bit?

# User Interface CONSTANTS
UI_TERMINAL_DELAY = 0.1         # Units are seconds
MAX_UI_DEALY = 2.0              # Units are seconds
FUNCTION_DELAY = 0.005          # Units are seconds
MIN_CAN_BUS_TIMESTEP = 0.001    # Units are seconds



# Dimensional unit CONSTANTS
PERCENTAGE_UNITS = '%'
MILLIMETER_UNITS = 'mm'
CENTIMETER_UNITS = 'cm'

# Datatbase Table Name CONSTANTS
VALID_SUPABASE_TABLE_NAMES = ["Users", "Cars", "EngineSounds", "TODO"]

# OBD-2 wiring CONSTANTS with pin number on ODB-2 connector, pin name, and color of wire
# MD = Manufacturer's Discretion https://en.wikipedia.org/wiki/On-board_diagnostics#OBD-II_diagnostic_connector
PIN01_MD = "RED_WIRE"
PIN02_SAE_J1850_LINE_BUS_PLUS = "WHITE_WIRE"
PIN03_MD = "ORANGE_WIRE"
PIN04_CHASSIS_GND = "BLUE_WIRE"
PIN05_SIGNAL_GND = "GREEN_WIRE"
PIN06_SAE_J2284_CAN_HIGH = "YELLOW_WIRE"
PIN07_K_LINE_ISO_9141_2__ISO_DIS_4230 = "BLACK_WIRE"
PIN08_MD = "PURPLE_WIRE"
PIN09_MD = "RED_BLACK_WIRE"
PIN10_SAE_J1850_LINE_BUS_MINUS = "WHITE_BLACK_WIRE"
PIN11_MD = "ORANGE_BLACK_WIRE"
PIN12_MD = "BLUE_BLACK_WIRE"
PIN13_MD = "GREEN_BLACK_WIRE"
PIN14_SAE_J2284_CAN_LOW = "YELLOW_BLACK_WIRE"
PIN15_L_LINE_ISO_9141_2__ISO_DIS_4230_4 = "BROWN_BLACK_WIRE"
PIN16_UNSWITCHED_VEHICLE_BATTERY_POSITIVE = "PURPLE_BLACK_WIRE"


class GlobalConstants:

    if __name__ == "__main__":
        print("Open GlobalConstants.py to see CONSTANTS used in the TesCustoms TesMuffler library")
