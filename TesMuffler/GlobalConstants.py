#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-12-27"
__doc__     = "Useful global constants for the entire TesCustoms TesMuffler library"
"""
# Global print() statement toggle for entire TesMuffler library
DEBUG_STATEMENTS_ON = True

# Vehicle make name CONTSTANTS - Yes these are sorted best to worst :)
TESLA = 0
APTERA = 1
KIA = 2
RIVIAN = 3
FORD = 4
VINFAST = 5

# Vehicle model name CONTSTANTS for vehicle makes above
MODEL_S = "S"
MODEL_3 = "3"
MODEL_X = "X"
MODEL_Y = "Y"
CYBER_TRUCK = "C"
ATV = "TESLA_ATV"
ROADSTER_V2 = "TESLA-ROADSTER-V2"
SEMI_TRUCK = "SEMI"
ALL_TESLAS = "S3XY-CARS"    # https://www.quora.com/Why-do-the-Tesla-models-spell-out-S3XY

MODEL_ = "SURYA"            #TODO Once model name is made public by Aptera Motors

R1T = "R1T"
R1S = "R1S"

F150_LIGHTNING = "F-150 LIGHTNING"
MACH_E = "MACH-E"

EV6 = "EV6"

VF6 = "VF6"
VF8 = "VF8"

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
GO_PEDAL_POSITION_CAN_BUS_IDENTIFIER = [0b11_111_111_111]           #TODO or 29bit?

BRAKE_PEDAL = 1                 # Pedal furthest left in automatic transmissions in UK and USA
BRAKE_PEDAL_POSITION_CAN_BUS_IDENTIFIER = [0b11_111_111_111]        #TODO or 29bit?

# Digital simulation of hardware CONSTANTS
TOP_GEAR = 5
MAX_RPM = 10_000

# Tesla CAN Bus CONSTANTS
VELOCITY_SENSOR_CAN_BUS_IDENTIFIER = [0b111_1111_1111]             #TODO or 29bit?
ENGINE_LOAD_CAN_BUS_IDENTIFIER = [0b111_1111_1111]                 #TODO or 29bit?
RPM_CAN_BUS_IDENTIFIER = [0b111_1111_1111]                         #TODO or 29bit?

ODDOMETER_CAN_BUS_IDENTIFIER = [0b111_1111_1111]                   #TODO or 29bit?
HYBRID_BATTERY_REMAINING_CAN_BUS_IDENTIFIER = [0b111_1111_1111]    #TODO or 29bit?

# User Interface CONSTANTS
UI_TERMINAL_DELAY = 0.1         # Units are seconds
MAX_UI_DELAY = 2.0              # Units are seconds
FUNCTION_DELAY = 0.005          # Units are seconds
MIN_CAN_BUS_TIMESTEP = 0.001    # Units are seconds
STANDARD_POLLING_RATE = 0.5     # Units are Hertz (0.5 Hz == 33.3 ms)
COLLECTING_DATA = False         # Software database flag to protect user data
SECURITY_TOGGLE_PIN = 4         # Hardware GPIO pin number to protect user data at hardware level TODO

# Text to Voice Audio CONSTANTS
FEMALE_ENGLISH_1 = "TODO"               # Used in VoiceGenerator http://www.festvox.org/flite/packed/flite-2.0/voices/
MALE_ENGLISH_1 = "TODO"                 # Used in VoiceGenerator http://www.festvox.org/flite/packed/flite-2.0/voices/
DIPHONE_MODEL_TECHNIQUE = "TODO"        # Most robotic sounding model, see https://github.com/MycroftAI/mimic1#notes
CLUSTER_GEN_MODEL_TECHNIQUE = "TODO"    # Most human sounding model with large file sizes and high CPU usage
HTS_MODEL_TECHNIQUE = "TODO"            # Semi-human sounding model with reduced files sizes

# Dimensional unit CONSTANTS
PERCENTAGE_UNITS = '%'
MILLIMETER_UNITS = 'mm'
CENTIMETER_UNITS = 'cm'

# Datatbase Table Name & HTTP error code  CONSTANTS
VALID_SUPABASE_TABLE_NAMES = ["Users", "Vehicles", "EngineSounds", "TODO"]      #TODO
DATABASE_OPERATION_FAILED = 400
DATABASE_OPERATION_SUCCESFULL = 200
SNAPSHOT_SIZE = 1000                    # OTA Update payload size [0x00] * 1000

# OBD-2 wiring CONSTANTS with pin number on ODB-2 connector, pin name, and color of wire
# MD = Manufacturer's Discretion https://en.wikipedia.org/wiki/On-board_diagnostics#OBD-II_diagnostic_connector
PIN01_MD = "BROWN_WIRE"
PIN02_SAE_J1850_LINE_BUS_PLUS = "BROWN_WHITE_WIRE"
PIN03_MD = "PURPLE_WIRE"
PIN04_CHASSIS_GND = "ORANGE_WIRE"                                   # 1A - TIE TOGETHER TO REDUCE GROUND LOOPS?
PIN05_SIGNAL_GND = "TEAL_WIRE"  # AKA BABY BLUE                     # 1B - TIE TOGETHER TO REDUCE GROUND LOOPS?
PIN06_SAE_J2284_CAN_HIGH = "GREEN_WIRE"                             # 2
PIN07_K_LINE_ISO_9141_2__ISO_DIS_4230 = "BLACK_WIRE"
PIN08_MD = "BLACK_WHITE_WIRE"
PIN09_MD = "RED_WHITE_WIRE"
PIN10_SAE_J1850_LINE_BUS_MINUS = "WHIRE_WIRE"
PIN11_MD = "YELLOW_WIRE"
PIN12_MD = "PINK_WIRE"
PIN13_MD = "GREY_WIRE"
PIN14_SAE_J2284_CAN_LOW = "GREEN_WHITE_WIRE"                        # 3
PIN15_L_LINE_ISO_9141_2__ISO_DIS_4230_4 = "DARK_BLUE_WIRE"
PIN16_UNSWITCHED_VEHICLE_BATTERY_POSITIVE = "RED_WIRE"              # 4

# ODB-2 python-odb protocol_name() and protocol_id()
SAE_J1850_PWM = 1
SAE_J1850_VPW = 2


class GlobalConstants:

    if __name__ == "__main__":
        print("Open GlobalConstants.py to see CONSTANTS used in the TesCustoms TesMuffler library")
