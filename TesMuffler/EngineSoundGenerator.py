#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-05-19"
__doc__     = "Class to create pitch varying audio in real-time on a low processing power CPUs"
"""

# http://www.mega-nerd.com/SRC/

# Allow for high-quality sample rate conversion
# https://pypi.org/project/samplerate/
import samplerate

# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

try:
    # Generate .txt data logging and custom terminal debugging output
    from DEBUG import *

    #TODO

except ImportError:
    currentProgramFilename = os.path.basename(__file__)
    TODO

class EngineSoundGenerator:

    # ICE car engine sound CONSTANTS
    MC_LAREN_F1 = "McLarenF1.mp3"
    FERRARI_LA_FERRARI = 2
    PORCSHE_911 = 3
    BMW_M4 = 4
    JAGUAR_E_TYPE_SERIES_1 = 5
    FORD_MODEL_T = 6
    MAX_SOUND_FILES = 6         # !!!UPDATE as more CONSTANTS are added

    def unitTest():
        print("STARTING EngineSoundGenerator.py Unit Test")

        # ESG = EngineSoundGenerator
        TestObject1 = EngineSoundGenerator(EngineSoundGenerator.BMW_M4)
        TestObject2 = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)

        #TODO
        assert()


        TestObject3 = EngineSoundGenerator(10)
        TestObject3 = EngineSoundGenerator("Ford_F_150.mp3")

        #TODO
        assert()


    def __init__(self, baseAudio):
        """
        Constructor to initialize an EngineSoundGenerator object
        Defaults to McLaren F1 if invalid baseAudio variable is passed

        Key arguments:
        self -- Newly created EngineSoundGenerator object
        baseAudio -- Starting audio .mp3 file to be modulated

        Return:
        New EngineSoundGenerator() object
        """

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(True, thisCodesFilename)

        if(baseAudio <= MAX_SOUND_FILES):
            self.selectedEngineSound = os.path.basename("/Sounds/ " + baseAudio)
        else:
            self.DebugObject.Dprint("OBJECT CREATION WARNING: You select an invalid base engine sound, we are defaulting to McLaren F1 engine sound")
            self.selectedEngineSound = os.path.basename("/Sounds/ " + MC_LAREN_F1)

    def __enter__(self):
        """
        TODO - See CocoDrink.py
        """

        print("in __enter")

        return self

    def __exit__(self):




    def adjustPitch():

    def adjustVolume():

    def setBaseAudio():

    def getBaseAudio():


if __name__ == "__main__":

    try:
        EngineSoundGenerator.unitTest()
    except NameError:
        print("Engine Sound Generator Unit Test failed :(")

    print("END of EngineSoundGenerator.py MAIN")
