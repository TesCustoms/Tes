#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "dev@blazesanders.com"
__status__  = "Development"
<<<<<<< HEAD
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

=======
__date__    = "Late Updated: 2022-10-14"
__doc__     = "Create pitch varying audio of a library of cars in real-time on low processing power CPUs"
"""

>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b
# Allow the control of the space-time fabric :)
# https://docs.python.org/3/library/time.html
import time

# Flexible event logging system for DEBUGGING, ERRORS, and INFO
# https://docs.python.org/3/library/logging.html
import logging

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
#TODO REMOVE? from subprocess import Popen, PIPE
from subprocess import check_call

try:  # Importing externally developed libraries

    # Allow 'dependency-free' playback of .wav audio on Linux, MacOS, & Windows
    # Often apt install libasound2-dev == yum install alsa-lib-devel is still needed
    # https://simpleaudio.readthedocs.io/en/latest/
    import simpleaudio as sa

    #TODO IF simpleaudio DONOT WORK
    # Allow for high-quality sample rate conversion
    # https://pypi.org/project/samplerate/
    #import samplerate

<<<<<<< HEAD
# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

# TODO INTERNAL LIBRARIES
try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    from Debug import *
=======
    #TODO IF BOTH simpleaudio and samplerate DONT WORK
    # Allow for playback of .mp3 audio on Linux, MacOS, & Windows
    # import  pyaudio
    # http://www.mega-nerd.com/SRC/
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b

    # Custom mp3 editting library base off Marco Arments Smart Speed
    # http://mpgedit.org/mpgedit/mpeg_format/mpeghdr.htm
    # TODO from mp3edit import *

except ImportError:  #TODO
    print("ERROR: The simpleaudio python module didn't import correctly!")
    executeInstalls = input("Would you like me to *** pip3 install simpleaudio *** for you (Y/N)? ")
    if(executeInstalls.upper() == "Y" or executeInstalls.upper() == "YES"):
        check_call("sudo apt install libasound2-dev", shell=True)
        check_call("pip install simpleaudio", shell=True)
    else:
        print("You didn't type Y or YES :)")
        print("Follow supabase manual install instructions at https://pypi.org/project/supabase/")


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

<<<<<<< HEAD
    # Debugging CONSTANTS
    DEBUG_STATEMENTS_ON = True

=======
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b
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

<<<<<<< HEAD
    def __init__(self, baseAudio):
        """ Constructor to initialize an EngineSoundGenerator object
            Defaults to McLaren F1 sound if invalid baseAudio variable is passed

        Args:
            self -- Newly created EngineSoundGenerator object
            baseAudio (str): CONSTANT filename of audio (.wav) file to be played and/or modulated
=======
    def __init__(self, baseAudioFilename):
        """Constructor to initialize an EngineSoundGenerator object
            Defaults to McLaren F1 sound if invalid baseAudioFilename input argument is passed

        Args:
            self -- Newly created EngineSoundGenerator object
            baseAudioFilename -- Starting audio .wav file to be modulated
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b

        Object instance variables:
            baseAudioFilename (str): Variable set to one of the valid Global CONSTANT sounds  
            engineSoundsDict (dictionary): A 'Collection' of valid sounds and their IDs
            engineSoundID (int): Unique ID to let embedded software to communicate with mobile app
            selectedEngineSoundObject (simpleaudio object): Filepath defined audio clip
            DebugObject(Debug object): Useful for debugging & data logging

        Returns:
            New EngineSoundGenerator() object
        """

        EngineSoundLog = logging.getLogger("EngineSound.log")
        #TODO REMOVE? logging.basicConfig(level=logging.INFO)

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
<<<<<<< HEAD
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
  
=======
            print(baseAudioFilename)
            self.engineSoundID = self.EngineSoundsDict[baseAudioFilename]
            print(self.engineSoundID)
            pathEnding = "./Sounds/" + baseAudioFilename

            # https://stackoverflow.com/questions/25672289/failed-to-open-file-file-wav-as-a-wav-due-to-file-does-not-start-with-riff-id
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(pathEnding)
            EngineSoundLog.debug("Engine sound found in dictionary")
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b
        except KeyError:
            EngineSoundLog.info("CONSTRUCTOR WARNING: You selected an invalid engine sound, defaulting to the McLaren F1")
            self.engineSoundID = EngineSoundGenerator.MC_LAREN_F1
            pathEnding = "./Sounds/McLarenF1.wav"
            self.baseAudioFilename = EngineSoundGenerator.MC_LAREN_F1
            self.EngineSoundWaveObject = sa.WaveObject.from_wave_file(pathEnding)

    def startAudioLoop(self):
<<<<<<< HEAD
        """ Play sound in loop forever
=======
        """
        Play sound in loop forever
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b
        """
        playObj = self.EngineSoundWaveObject.play()
        playObj.wait_done()

    def startAudio(self):
        """
        Play sound in loop forever
        """
        playObj = self.EngineSoundWaveObject.play()

        return playObj

<<<<<<< HEAD
    def stopAudioLoop(self):
        """ Stop sound playing during last call to startAudioLoop() function
        """
        self.EngineSoundWaveObject.stop()
=======
    def stopAudio(self, playObj):
        """
        Stop sound playing in last wait_done() function call
        """
        #stop_obj = self.EngineSoundWaveObject.stop()
        stop_obj = playObj.stop()
        #sa.stopall()
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b

    def adjustPitch(self):
        """ TODO WILL REQUIRE LIBRARY OTHER THEN SIMPLEAUDIO
        """

        print("TODO")

<<<<<<< HEAD

    def adjustVolume(self, newLevel):
        """ TODO
=======
    def adjustVolume():
        """
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b
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

<<<<<<< HEAD

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
=======
    def setbaseAudioFilename(self, newSound):
        """
        """

        self.baseAudioFilename = newSound

    def getbaseAudioFilename(self):
        """

        Args:
            NONE
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b

        Returns:

        """
        return int(self.engineSoundID)


<<<<<<< HEAD
    try:
        EngineSoundGenerator.unitTest()
    
    except AssertionError as error: #NameError:
        print("Engine Sound Generator Unit Test failed :(")
=======
if __name__ == "__main__":
>>>>>>> b15dd0a69ddf2ae0e3525153edcd12ecbc42638b

    EngineSoundGenerator.unitTest()
