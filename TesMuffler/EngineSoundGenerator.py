#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-07-17"
__doc__     = "Class to create pitch varying audio in real-time on a low processing power CPUs"
"""

# Allow 'dependency-free' playback of .wav audio on Linux, MacOS, & Windows
# https://simpleaudio.readthedocs.io/en/latest/
import simpleaudio as sa

#TODO IF simpleaudio DONOT WORK
# Allow for high-quality sample rate conversion
# https://pypi.org/project/samplerate/
#import samplerate

#TODO IF BOTH simpleaudio and samplerate DONT WORK
# Allow for playback of .mp3 audio on Linux, MacOS, & Windows
# import  pyaudio

# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os


try:
    # Generate .txt data logging and custom terminal debugging output
    from Debug import *
    # Custom mp3 editting library base off Marco Arments Smart Speed
    # http://mpgedit.org/mpgedit/mpeg_format/mpeghdr.htm
    from mp3edit import *
    #TODO

except ImportError:
    print("Debug didn't import correctly, please verify that Debug.py is in TODO")
	#TODO


class EngineSoundGenerator:
	"""Audio playing class that calls into bluetooth stream class
	"""
	# Acronymn list: ESG = EngineSoundGenerator

	# ICE car engine sound CONSTANTS
	MC_LAREN_F1 = "McLarenF1.wav"
	LA_FERRARI = "LaFerrari.wav"
	PORCSHE_911 = "Porcshe911.wav"
	BMW_M4 = "BMW_M4.wav"
	JAGUAR_E_TYPE_SERIES_1 = "JaguarEtypeSeries1.wav"
	FORD_MODEL_T = "FordModelT.wav"
	FORD_MUSTANG_GT350 = "FordMustangGT350.wav"

	#Debugging CONSTANTS
	DEBUG_STATEMENTS_ON = True


	def unitTest():
    
        	print("STARTING EngineSoundGenerator.py Unit Test")

        	TestObject1 = EngineSoundGenerator(EngineSoundGenerator.MC_LAREN_F1)
        	#TODO assert()

	        TestObject2 = EngineSoundGenerator(EngineSoundGenerator.BMW_M4)
        	#TODO assert()

	        TestObject3 = EngineSoundGenerator(10)
       		 #TODO assert()

	        TestObject4 = EngineSoundGenerator(6.9)
	        #TODO assert()

        	TestObject5 = EngineSoundGenerator('Ford_F_150.mp3')
	        #TODO assert()

        	print("EngineSoundGenerator.py Unit Test COMPLETE")


    def __init__(self, baseAudio):
        """Constructor to initialize an EngineSoundGenerator object
           Defaults to McLaren F1 if invalid baseAudio variable is passed

        Args:
        	self -- Newly created EngineSoundGenerator object
        	baseAudio -- Starting audio .mp3 file to be modulated

        Object instance variables:
        	engineSoundsDict -- DICTIONARY: A Collection of valid sounds and their IDs
        	engineSoundID -- INT: Unique ID for TODO
        	selectedEngineSoundObject -- OBJECT: Audio ojbect defined a filepath to a audio clip
        	DebugObject -- Debug.py OBJECT: Useful for debugging & data logging

        Returns:
        	New EngineSoundGenerator() object
        """

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(EngineSoundGenerator.DEBUG_STATEMENTS_ON, thisCodesFilename)

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
            self.engineSoundID = self.EngineSoundsDict[baseAudio]
            self.filePath = os.path.basename("/Sounds/" + baseAudio)     				#TODO space after "/Sounds/ " ?
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(self.filePath)
            self.DebugObject.Dprint("Engine sound found in dictionary")
        except KeyError:
            message = "CONSTRUCTOR WARNING: You select an invalid engine sound, defaulting to the McLaren F1"
            self.DebugObject.Lprint(message)
            self.engineSoundID =  EngineSoundGenerator.MC_LAREN_F1
            self.filePath = os.path.basename("/Sounds/McLarenF1.wav")
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(self.filePath)


    def startAudioLoop():
        """Play sound in loop forever
        """
        self.EngineSoundObject.wait_done()

    def stopAudioLoop():
        """Stop sound playing in last wait_done() function
        """
        self.EngineSoundObject.stop()

    def adjustPitch():
        """
        """

        print("TODO")


    def adjustVolume():
        """
        """

        print("TODO REMOVE SINCE CAR SHOULD CONTROL VOLUME LEVEL")


    def setBaseAudio(newSound):
        """
        """

        self.baseAudio = newSound


    def getBaseAudio():
        """
        """
        self.engineSoundID = self.EngineSoundsDict[baseAudio]

        return self.baseAudio


if __name__ == "__main__":

    try:
        EngineSoundGenerator.unitTest()
    except AssertionError as error: #NameError:
        print("Engine Sound Generator Unit Test failed :(")

    print("END of EngineSoundGenerator.py MAIN method")
