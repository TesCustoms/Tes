#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-22"
__doc__     = "Create pitch varying audio real-time on low processing power CPUs"
"""

try:
    # Allow 'dependency-free' playback of .wav audio on Linux, MacOS, & Windows
    # https://simpleaudio.readthedocs.io/en/latest/
    import simpleaudio as sa

    #TODO IF simpleaudio DOES NOT WORK
    # Allow for high-quality sample rate conversion
    # https://pypi.org/project/samplerate/
    #import samplerate

    #TODO IF BOTH simpleaudio and samplerate DONT WORK
    # Allow for playback of .mp3 audio on Linux, MacOS, & Windows
    # import  pyaudio

except ModuleNotFoundError:
    print("Audio process library (simpleaudio or TODO) was not pip installed  correctly")
    print("Please verify that the virutalenv 'TeslaDevEnv' is running using the source command")
    print("OR if easier for you run the command 'pip install simpleaudio' or TODO")
    #TODO

# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

# TODO INTERNAL LIBRARIES
try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    from Debug import *

    # Custom mp3 editting library base off Marco Arments Smart Speed
    # http://mpgedit.org/mpgedit/mpeg_format/mpeghdr.htm
    from mp3edit import *
    #TODO

except ImportError:
    print("Debug.py or mp3edit.py didn't import correctly")
    print("Please verify that those files are in same directory as the EngineSoundGenerator.py")
    #TODO

class EngineSoundGenerator:
    """ Acronymn list: 
        ESG = EngineSoundGenerator
    """

    # ICE car engine sound CONSTANTS
    MC_LAREN_F1 = "McLarenF1.wav"
    LA_FERRARI = "LaFerrari.wav"
    PORCSHE_911 = "Porcshe911.wav"
    BMW_M4 = "BMW_M4.wav"
    JAGUAR_E_TYPE_SERIES_1 = "JaguarEtypeSeries1.wav"
    FORD_MODEL_T = "FordModelT.wav"
    FORD_MUSTANG_GT350 = "FordMustangGT350.wav"

    # Debugging CONSTANTS
    DEBUG_STATEMENTS_ON = True

    def unitTest():
        print("STARTING EngineSoundGenerator.py Unit Test")

        TestObject1 = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)
        assert TestObject1.getBaseAudio == EngineSoundGenerator.MC_LAREN_F1
        assert TestObject1.startAudioLoop

        TestObject2 = EngineSoundGenerator(EngineSoundGenerator.BMW_M4)
        assert TestObject2.startAudioLoop
        assert TestObject2.stopAudioLoop

        TestObject3 = EngineSoundGenerator(10)
        assert TestObject3, "Invalid engine sound ID - Please use a global CONSTANT in EngineSoundGenerator.py"

        TestObject4 = EngineSoundGenerator(6.9)
        assert TestObject4, "Invalid engine sound ID - Please use a global CONSTANT in EngineSoundGenerator.py"

        TestObject5 = EngineSoundGenerator("Ford_F_150.mp3")
        assert TestObject5, "Invalid engine sound STRING - Please use a global CONSTANT in EngineSoundGenerator.py"

        TestObject6 = EngineSoundGenerator("JaguarEtypeSeries1.wav")
        assert TestObject6
        
        print("EngineSoundGenerator.py Unit Test COMPLETE")


    def __init__(self, baseAudio):
        """ Constructor to initialize an EngineSoundGenerator object
            Defaults to McLaren F1 sound if invalid baseAudio variable is passed

        Args:
            self -- Newly created EngineSoundGenerator object
            baseAudio (str): CONSTANT filename of audio (.wav) file to be played and/or modulated

        Object instance variables:
            baseAudioFilename (str): Variable set to one of the valid Global CONSTANT sounds  
            engineSoundsDict (dictionary): A 'Collection' of valid sounds and their IDs
            engineSoundID (int): Unique ID to let embedded software to communicate with mobile app
            selectedEngineSoundObject (simpleaudio object): Filepath defined audio clip
            DebugObject(Debug object): Useful for debugging & data logging

        Returns:
            New EngineSoundGenerator() object
        """

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(EngineSoundGenerator.DEBUG_STATEMENTS_ON, thisCodesFilename)

        # UPDATE this dictionary, EngineSoundGenerator.py global CONSTANTS,
        # and the Tes/TesMuffler/Sounds folder to add new engine sounds
        self.EngineSoundsDict = {
            EngineSoundGenerator.MC_LAREN_F1: 0,
            EngineSoundGenerator.LA_FERRARI: 1,
            EngineSoundGenerator.PORCSHE_911: 2,
            EngineSoundGenerator.BMW_M4: 3,
            EngineSoundGenerator.JAGUAR_E_TYPE_SERIES_1: 4,
            EngineSoundGenerator.FORD_MODEL_T: 5,
            EngineSoundGenerator.FORD_MUSTANG_GT350: 6
        }

        # Use dictionary lookup to check for valid baseAudio CONSTRUCTOR parameter
        try:
            self.engineSoundID = self.EngineSoundsDict[baseAudio]
            ##self.filePath = os.path.basename("/Sounds/" + baseAudio)     	#TODO space after "/Sounds/ " ?
            ##self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(self.filePath)
            pathEnding = "./Sounds/" + baseAudio
            self.baseAudioFilename = baseAudio
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(pathEnding)
            self.DebugObject.Dprint("Engine sound found in dictionary")
        
        except NameError:
            message = "CONSTRUCTOR ERROR: Shutting down program since audio process library is NOT installed")
            self.DebugObject.Lprint(message)
            check_call("exit()", shell=True)  #TODO DOES THIS WORK
  
        except KeyError:
            message = "CONSTRUCTOR WARNING: You select an invalid engine sound, defaulting to the McLaren F1"
            self.DebugObject.Lprint(message)
            self.engineSoundID =  EngineSoundGenerator.MC_LAREN_F1
            ##self.filePath = os.path.basename("/Sounds/McLarenF1.wav")
            ##self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(self.filePath)
            pathEnding = "./Sounds/McLarenF1.wav"
            self.baseAudioFilename = EngineSoundGenerator.MC_LAREN_F1
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(pathEnding)
 

    def startAudioLoop(self):
        """ Play sound in loop forever
        """
        playObj = self.EngineSoundWaveObject.play()
        playObj.wait_done()


    def stopAudioLoop(self):
        """ Stop sound playing during last call to startAudioLoop() function
        """
        self.EngineSoundWaveObject.stop()

    def adjustPitch(self):
        """ TODO WILL REQUIRE LIBRARY OTHER THEN SIMPLEAUDIO
        """

        print("TODO")


    def adjustVolume(self, newLevel):
        """ TODO
        """
        if(newLevel == GC.UP):
        elif(newLevel == GC.DOWN):
        elif(0 <= newLevel or newLevel <= 100):
            volume = newLevel
        elif(100 < newLevel):
            volume = 100
        else:
           self.DebugObject = 

        print("TODO REMOVE SINCE CAR SHOULD CONTROL VOLUME LEVEL")


    def setNeweSound(self, newSound):
        """ Change sound configured to play during the next startAudioLoop() function call
        
        Args:
            newSound (str): CONSTANT filename of audio file to be played and/or modulated
        
        Returns:
            NOTHING
        """

        # Use dictionary lookup to check for valid baseAudio CONSTRUCTOR parameter
        try:
            self.engineSoundID = self.EngineSoundsDict[newSound]
            pathEnding = "./Sounds/" + newSound
            self.baseAudioFilename = newSound
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(pathEnding)
            self.DebugObject.Dprint("Engine sound found in dictionary")
        
        except KeyError:
            message = "WARNING: New sound was NOT set. Keeping sound set to ", self.baseAudio
            self.DebugObject.Lprint(message)


    def getBaseAudio(self):
        """ Determine sound configured to play during the next startAudioLoop() function call

        Args:
            NONE
        
        Returns:
            A EngineSoundGenerator CONSTANT of engine sound set to play
        """

        return self.baseAudioFilename


if __name__ == "__main__":

    try:
        EngineSoundGenerator.unitTest()
    
    except AssertionError as error: #NameError:
        print("Engine Sound Generator Unit Test failed :(")

    print("END of EngineSoundGenerator.py MAIN method")
