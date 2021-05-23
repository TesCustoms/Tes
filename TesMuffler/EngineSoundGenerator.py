#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-05-22"
__doc__     = "Class to create pitch varying audio in real-time on a low processing power CPUs"
"""

# http://www.mega-nerd.com/SRC/
# https://github.com/jiaaro/pydub
# https://people.csail.mit.edu/hubert/pyaudio/
# https://simpleaudio.readthedocs.io/en/latest/
# https://realpython.com/playing-and-recording-sound-python/

# Allow for high-quality sample rate conversion
# https://pypi.org/project/samplerate/
import samplerate

# Allow for playback of .mp3 audio on Linux, MacOS, & Windows
#TODO import  pyaudio

# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

try:
    # Generate .txt data logging and custom terminal debugging output
    from Debug import *

    #TODO

except ImportError:
    currentProgramFilename = os.path.basename(__file__)
    #TODO


class EngineSoundGenerator:

    # Acronymn list: ESG = EngineSoundGenerator

    # ICE car engine sound CONSTANTS
    MC_LAREN_F1 = "McLarenF1.mp3"
    LA_FERRARI = "LaFerrari.mp3"
    PORCSHE_911 = "Porcshe911.mp3"
    BMW_M4 = "BMW_M4.mp3"
    JAGUAR_E_TYPE_SERIES_1 = "JaguarEtypeSeries1.mp3"
    FORD_MODEL_T = "FordModelT"
    FORD_MUSTANG_GT350 = "FordMustangGT350.mp3"


    def unitTest():
        print("STARTING EngineSoundGenerator.py Unit Test")

        TestObject1 = EngineSoundGenerator(EngineSoundGenerator.BMW_M4)
        #TODO assert()

        TestObject2 = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)
        #TODO assert()

        TestObject3 = EngineSoundGenerator(10)
        #TODO assert()

        TestObject4 = EngineSoundGenerator(6.9)
        #TODO assert()

        TestObject5 = EngineSoundGenerator('Ford_F_150.mp3')
        #TODO assert()

        print("EngineSoundGenerator.py Unit Test COMPLETE")


    def __init__(self, baseAudio):
        """
        Constructor to initialize an EngineSoundGenerator object
        Defaults to McLaren F1 if invalid baseAudio variable is passed

        Key arguments:
        self -- Newly created EngineSoundGenerator object
        baseAudio -- Starting audio .mp3 file to be modulated

        Object instance variables:
        engineSoundsDict -- DICTIONARY: A Collection of valid sounds and their IDs
        engineSoundID -- INT: Unique ID for TODO
        selectedEngineSound -- STRING: Full filepath and filename to sound
        DebugObject -- Debug.py OBJECT: Useful for debugging & data logging

        Return:
        New EngineSoundGenerator() object
        """

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(True, thisCodesFilename)

        # UPDATE this dictionary, EngineSoundGenerator.py global CONSTANTS,
        # and the Tes/TesMuffler/Sounds folder to add new sounds
        self.EngineSoundsDict = {
            "McLarenF1.mp3": 0,
            "LaFerrari.mp3": 1,
            "Porcshe911.mp3": 2,
            "BMW_M4.mp3": 3,
            "Jaguar_E_Type_Series_1.mp3": 4,
            "FordModel_T.mp3": 5,
            "FordMustangGT350R.mp3": 6
        }

        # Check for valid constructor parameters
        try:
            self.engineSoundID = self.EngineSoundsDict[baseAudio]
            self.selectedEngineSound = os.path.basename("/Sounds/ " + baseAudio)
            self.DebugObject.Dprint(self.selectedEngineSound)
        except KeyError:
            message = "CONSTRUCTOR WARNING: You select an invalid engine sound, defaulting to the McLaren F1"
            self.DebugObject.Lprint(message)
            self.selectedEngineSound = os.path.basename("/Sounds/ " + EngineSoundGenerator.MC_LAREN_F1)


    def adjustPitch():
        """
        """

        print("TODO")


    def adjustVolume():
        """
        """

        print("TODO")


    def setBaseAudio(newSound):
        """
        """

        self.baseAudio = newSound


    def getBaseAudio():
        """
        """

        return self.baseAudio


if __name__ == "__main__":

    try:
        EngineSoundGenerator.unitTest()
    except AssertionError as error: #NameError:
        print("Engine Sound Generator Unit Test failed :(")

    print("END of EngineSoundGenerator.py MAIN method")
