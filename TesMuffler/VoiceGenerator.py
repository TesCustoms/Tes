#!/usr/bin/env python3
"""
__authors__    = ["Blaze Sanders", "TODO]
__date__       = "2022/12/30"
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

# Flexible event logging system for DEBUGGING, ERRORS, and INFO
# https://docs.python.org/3/library/logging.html
import logging

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
from subprocess import check_call

try:
    pass

except ImportError:
    print("ERROR: The TODO python module didn't import correctly!")
    executeInstalls = input("Would you like me to *** pip3 install TODO *** for you (Y/N)? ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("sudo apt install TODO", shell=True)
        check_call("pip install TODO", shell=True)
    else:
        print("You didn't type Y or YES :)")
        print("Follow TODO manual install instructions at https://TODO")

class VoiceGenerator:

    CONSTANT = "TODO"


    def unitTest():
        print("STARTING VoiceGenerator.py Unit Test")

        TestObject1 = VoiceGenerator()
        assert TestObject1, "TODO"

        print("EngineSoundGenerator.py Unit Test COMPLETE")

    def __init__(self, voiceID):
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


    def sayText(self, text):
        fullCommand = "./mimic -t " + text
        check_call(fullCommand)


    def sayFile(self, text, filename="sayFile.wav"):
        fullCommand = "./mimic -t " + text
        check_call(fullCommand)


if __name__ == "__main__":

    VoiceGenerator.unitTest()
