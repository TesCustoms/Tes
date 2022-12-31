#!/usr/bin/env python3
"""
__authors__    = ["Blaze Sanders", "TODO]
__date__       = "2022/12/31"
__deprecated__ = False
__doc__        = "Create semi-human / semi-robotic voice audio to say hello (and other words) to users like 1984 Apple Macintosh"
__email__      = "dev@blazesanders.com"
__license__    = "MIT"
__status__     = "Development"
"""

# Mimic is a fast, lightweight Text-to-speech engine developed by Mycroft A.I. and VocaliD, based on Carnegie Mellon University’s Flite (Festival-Lite) software.
# Mimic takes in text and reads it out loud to create a high quality voice.
# https://github.com/MycroftAI/mimic1
# sudo apt-get install gcc make pkg-config automake libtool libasound2-dev

# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

# Flexible event logging system for DEBUGGING, ERRORS, and INFO
# https://docs.python.org/3/library/logging.html
import logging

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
from subprocess import check_call

try:
    pass #import TODO

except ImportError:
    print("ERROR: The Mimic Mycroft TTS Engine didn't install correctly!")
    executeInstalls = input("Would you like me to *** sudo apt-get install gcc make pkg-config automake libtool libasound2-dev *** on the Raspberry Pi for you (Y/N)? ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("sudo apt install gcc make pkg-config automake libtool libasound2-dev", shell=True)
        check_call("BUILD? TODO", shell=True) #https://github.com/MycroftAI/mimic1#build
    else:
        print("You didn't type Y or YES :)")
        print("Follow Mimic1 manual install instructions at https://github.com/MycroftAI/mimic1#requirements")

# Useful global constants for the entire TesCustoms TesMuffler library
import GlobalConstants as GC


class VoiceGenerator:

    def unitTest():
        print("STARTING VoiceGenerator.py Unit Test")

        TestObject1 = VoiceGenerator(GC.MALE_ENGLISH_1, GC.DIPHONE_MODEL_TECHNIQUE)
        TestObject2 = VoiceGenerator(GC.MALE_ENGLISH_1, GC.CLUSTER_GEN_MODEL_TECHNIQUE)
        TestObject3 = VoiceGenerator(GC.MALE_ENGLISH_1, GC.HTS_MODEL_TECHNIQUE)
        TestObject4 = VoiceGenerator(GC.FEMALE_ENGLISH_1, GC.DIPHONE_MODEL_TECHNIQUE)
        TestObject5 = VoiceGenerator(GC.FEMALE_ENGLISH_1, GC.CLUSTER_GEN_MODEL_TECHNIQUE)
        TestObject6 = VoiceGenerator(GC.FEMALE_ENGLISH_1, GC.HTS_MODEL_TECHNIQUE)
        TestObject7 = VoiceGenerator()
        TestObject8 = VoiceGenerator(1, "HTS")
        TestObject9 = VoiceGenerator("MALE", 2)

        TestObject1.sayText("Hello World")
        TestObject1.createSayFile("Hello World")
        time.sleep(GC.MAX_UI_DELAY)

        TestObject2.sayText("Hello World")
        TestObject2.createSayFile("Hello World")
        time.sleep(GC.MAX_UI_DELAY)

        TestObject3.sayText("Hello World")
        TestObject3.createSayFile("Hello World")
        time.sleep(GC.MAX_UI_DELAY)

        TestObject4.sayText("I'm sorry Dave, I can't do that!")
        TestObject4.createSayFile("I'm sorry Dave, I can't do that!")
        time.sleep(GC.MAX_UI_DELAY)

        TestObject5.sayText("I'm sorry Dave, I can't do that!")
        TestObject5.createSayFile("I'm sorry Dave, I can't do that!")
        time.sleep(GC.MAX_UI_DELAY)

        TestObject6.sayText("I'm sorry Dave, I can't do that!")
        TestObject6.createSayFile("I'm sorry Dave, I can't do that!")
        time.sleep(GC.MAX_UI_DELAY)

        assert TestObject7, "Default VoiceGenerator.py object creation failed"
        assert TestObject8, "Invalid parameter(s) passed to VoiceGenerator.py __init__() function"
        assert TestObject9, "Invalid parameter(s) passed to VoiceGenerator.py __init__() function"

        print("VoiceGenerator.py Unit Test COMPLETE")

    def __init__(self, voiceID=GC.MALE_ENGLISH_1, speechModelingTechnique=GC.CLUSTER_GEN_MODEL_TECHNIQUE):
        """Constructor to initialize an VoiceGenerator object

        Args:
            self -- Newly created VoiceGenerator object
            voiceID -- TODO

        Object instance variables: TODO
            engineSoundsDict -- DICTIONARY: A Collection of valid sounds and their IDs
            engineSoundID -- INT: Unique ID for TODO
            selectedEngineSoundObject -- OBJECT: Audio ojbect defined a filepath to a audio clip
            DebugObject -- Debug.py OBJECT: Useful for debugging & data logging

        Returns:
            New VoiceGenerator() object
        """

        VoiceLog = logging.getLogger("VoiceSound.log")

        if(voiceID == GC.FEMALE_ENGLISH_1):
            pass
        elif(voiceID == GC.MALE_ENGLISH_1):
            pass
        else:
            pass

        if(speechModelingTechnique == GC.DIPHONE_MODEL_TECHNIQUE):
            pass
       # https://github.com/MycroftAI/mimic1#usage

    def sayText(self, text):
        """Pay sound using audio device
           https://github.com/MycroftAI/mimic1#usage

        Args:
            text -- STRING: 

        Returns:
            NOTHING
        """
        fullCommand = "./mimic -t " + text.strip()
        #TODO check_call(fullCommand)


    def createSayFile(self, text, filename="SayFile.wav"):
        """Create file to play on audio device at later time

        Args:
            text -- STRING: 
            filename -- STRING:

        Returns:
            Output the wave file in RIFF format (often called .wav).
        """
        filenameFileExtensionTuple = filename.partition(".")   # Tuple will be ['filename', '.', 'extension']
        if(filenameFileExtensionTuple[2].upper() != "WAV"):
            pass #LOG ERROR, CODE CAN ONLY PLAY .wav files
        else:
            fullCommand = "./mimic -t '" + text.strip() + "' -o " + filename.strip()
            #TODO check_call(fullCommand)


if __name__ == "__main__":

    VoiceGenerator.unitTest()
