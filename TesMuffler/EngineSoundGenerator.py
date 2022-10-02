#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2022-10-01"
__doc__     = "Create pitch varying audio of a library of cars in real-time on low processing power CPUs"
"""

# Allow 'dependency-free' playback of .wav audio on Linux, MacOS, & Windows
# Often apt install libasound2-dev == yum install alsa-lib-devel is still needed
# https://simpleaudio.readthedocs.io/en/latest/
import simpleaudio as sa

#TODO IF simpleaudio DONOT WORK
# Allow for high-quality sample rate conversion
# https://pypi.org/project/samplerate/
#import samplerate

#TODO IF BOTH simpleaudio and samplerate DONT WORK
# Allow for playback of .mp3 audio on Linux, MacOS, & Windows
# import  pyaudio
# http://www.mega-nerd.com/SRC/

# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

# Flexible event logging system for DEBUGGING, ERRORS, and INFO 
# https://docs.python.org/3/library/logging.html
import logging

try:
    # Custom mp3 editting library base off Marco Arments Smart Speed
    # http://mpgedit.org/mpgedit/mpeg_format/mpeghdr.htm
    from mp3edit import *
    #TODO

except ImportError:
    print("mp3edit.py didn't import correctly")
    print("Please verify that those files are in same directory as the EngineSoundGenerator.py")


class EngineSoundGenerator:
    # Acronymn list: ESG = EngineSoundGenerator

    # ICE car engine sound CONSTANTS
    MC_LAREN_F1 = "McLarenF1.wav"
    LA_FERRARI = "LaFerrari.wav"
    PORCSHE_911 = "Porcshe911.wav"
    BMW_M4 = "BMW_M4.wav"
    JAGUAR_E_TYPE_SERIES_1 = "JaguarEtypeSeries1.wav"
    FORD_MODEL_T = "FordModelT.wav"
    FORD_MUSTANG_GT350 = "FordMustangGT350.wav"

    def unitTest():
        print("STARTING EngineSoundGenerator.py Unit Test")

        TestObject1 = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)
        assert TestObject1.getbaseAudioFilename() == TestObject1.EngineSoundsDict[EngineSoundGenerator.MC_LAREN_F1]
        playObj = TestObject1.startAudio()
        time.sleep(1.5)
        TestObject1.stopAudio(playObj)

        # TestObject2 = EngineSoundGenerator(EngineSoundGenerator.BMW_M4)
        # assert TestObject2.startAudioLoop
        # assert TestObject2.stopAudioLoop

        TestObject3 = EngineSoundGenerator(10)
        playObj = TestObject3.startAudio()
        time.sleep(1.5)
        TestObject3.stopAudio(playObj)
        # assert TestObject3, "Invalid engine sound ID - Please use a global CONSTANT in EngineSoundGenerator.py"

        TestObject4 = EngineSoundGenerator(6.9)
        assert TestObject4, "Invalid engine sound ID - Please use a global CONSTANT in EngineSoundGenerator.py"

        TestObject5 = EngineSoundGenerator("Ford_F_150.mp3")
        assert TestObject5, "Invalid engine sound STRING - Please use a global CONSTANT in EngineSoundGenerator.py"

        # TestObject6 = EngineSoundGenerator(EngineSoundGenerator("JaguarEtypeSeries1.wav"))
        # assert TestObject6

        print("EngineSoundGenerator.py Unit Test COMPLETE")

    def __init__(self, baseAudioFilename):
        """Constructor to initialize an EngineSoundGenerator object
            Defaults to McLaren F1 sound if invalid baseAudioFilename input argument is passed

        Args:
            self -- Newly created EngineSoundGenerator object
            baseAudioFilename -- Starting audio .wav file to be modulated

        Object instance variables:
            engineSoundsDict -- DICTIONARY: A Collection of valid sounds and their IDs
            engineSoundID -- INT: Unique ID for TODO
            selectedEngineSoundObject -- OBJECT: Audio ojbect defined a filepath to a audio clip
            DebugObject -- Debug.py OBJECT: Useful for debugging & data logging

        Returns:
            New EngineSoundGenerator() object
        """

        EngineSoundLog = logging.getLogger("EngineSound.log")
        #TODO REMOVE? logging.basicConfig(level=logging.INFO)

        # UPDATE this dictionary, EngineSoundGenerator.py global CONSTANTS,
        # and the Tes/TesMuffler/Sounds folder to add new sounds
        self.EngineSoundsDict = {
            EngineSoundGenerator.MC_LAREN_F1: 0,
            EngineSoundGenerator.LA_FERRARI: 1,
            EngineSoundGenerator.PORCSHE_911: 2,
            EngineSoundGenerator.BMW_M4: 3,
            EngineSoundGenerator.JAGUAR_E_TYPE_SERIES_1: 4,
            EngineSoundGenerator.FORD_MODEL_T: 5,
            EngineSoundGenerator.FORD_MUSTANG_GT350: 6
        }

        # Check for valid constructor parameters
        try:
            print(baseAudioFilename)
            self.engineSoundID = self.EngineSoundsDict[baseAudioFilename]
            print(self.engineSoundID)
            pathEnding = "./Sounds/" + baseAudioFilename
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(pathEnding)
            EngineSoundLog.debug("Engine sound found in dictionary")
        except KeyError:
            EngineSoundLog.info("CONSTRUCTOR WARNING: You selected an invalid engine sound, defaulting to the McLaren F1")
            self.engineSoundID = EngineSoundGenerator.MC_LAREN_F1
            pathEnding = "./Sounds/McLarenF1.wav"
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(pathEnding)

    def startAudioLoop(self):
        """
        Play sound in loop forever
        """
        playObj = self.EngineSoundWaveObject.play()
        playObj.wait_done()

    def startAudio(self):
        """
        Play sound in loop forever
        """
        playObj = self.EngineSoundWaveObject.play()

        return playObj

    def stopAudio(self, playObj):
        """
        Stop sound playing in last wait_done() function call
        """
        #stop_obj = self.EngineSoundWaveObject.stop()
        stop_obj = playObj.stop()
        #sa.stopall()

    def adjustPitch():
        """
        """

        print("TODO")

    def adjustVolume():
        """
        """

        print("TODO REMOVE SINCE CAR SHOULD CONTROL VOLUME LEVEL")

    def setbaseAudioFilename(self, newSound):
        """
        """

        self.baseAudioFilename = newSound

    def getbaseAudioFilename(self):
        """

        Args:
            NONE

        Returns:

        """
        return int(self.engineSoundID)


if __name__ == "__main__":

    EngineSoundGenerator.unitTest()
