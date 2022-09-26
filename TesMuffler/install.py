#!/usr/bin/env python3
"""
__author__ =  "Blaze Sanders"
__email__ =   "blaze.d.a.sanders@gmail.com"
__company__ = "Humanity"
__status__ =  "Development"
__date__ =    "Late Updated: 2021-07-31"
__doc__ =     "Setup a new TesMuffler dev enviroment using VirtualEnv"
"""


# Hardware that code can run on CONSTANTS (WINDOWS IS NOT SUPPORTED!)
PI_4     = "Pi4"     # Raspberry Pi 4
RP_2040  = "RP2040"  # Arduino Microcontroller
PI_PICO  = "PiPico"  # Raspbery Pi Microntroller
ESP_32   = "ESP32"   # EspressIf IOT Microcontoller
LINUX_PC = "LinuxPC" # Intel CPU Personal Computer
MAC_OS   = "M1Mac"   # M1 Mac Personal Computer


# Allow for easy command-line install of all TesMuffler dependencies
# https://docs.python.org/3/library/argparse.html
import argparse

# Allow pausing of code so that programmers can read terminal output
# https://docs.python.org/3/library/time.html
import time

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call


if __name__ == "__main__":

	parser = argparse.ArgumentParser(prog = "Trying to install TesMuffler app", description = __doc__, add_help=True)
	parser.add_argument("-d", "--device", type=str, default= PI_4, choices=[PI_4, RP_2040, PI_PICO, LINUX_PC, MAC_OS], help="Select the hardware code is running on")
	#TODO Add to TesMufflerDriver.py - parser.add_argument("-t", "--trace", type=int, default=0, help="Program trace level.")
	args = parser.parse_args()

	hardware = args.device

	# Clear terminal and prompt user of next steps
	check_call("clear",shell=True)
	print("Starting TesMuffler install inside a virtual enviroment and performing system update!")
	print("Press CTRL-Z now to cancel install and system updates")
	for countdown in range(10, 0, -1):
		print(countdown)
		time.sleep(1)
	print("LIFTOFF!")

	# Check and update your system
	check_call("sudo apt update", shell=True)
	check_call("sudo apt upgrade", shell=True)
	# WARNING: If update fails here read the manual page
	# using the "man apt-secure" command
	# and then try the "sudo apt-get --allow-unauthenticated upgrade" command
	# and then trt sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys YOUR_KEY

	# Install PIP3 and update setuptools
	# Flask GUI's (TODO FUTURE WORK) require Python 3 or above
	check_call("sudo apt install python3-pip", shell=True)
	check_call("pip install --upgrade pip setuptools", shell=True)


	# Start autoconfiguring a virtual enviroment like a good programmer should :)
	# https://www.geeksforgeeks.org/python-virtual-environment/
	check_call("sudo apt install python3-virtualenv", shell=True)
	check_call("virtualenv --version", shell=True)
	time.sleep(2)
	check_call("virtualenv TesMufflerDevEnv", shell=True)
	# Specifiy Python 3 interpreter to stay away from all things Python 2!
	check_call("virtualenv -p /usr/bin/python3 TesMufflerDevEnv", shell=True)

	# Start / activate the virtual enviroment setup above
	# Important to do this before any "pip3 install" commands
	try:
		#TODO https://www.reddit.com/r/Python/comments/5lift9/how_to_activatedeactivate_virtualenv_on_linux/
		check_call("source TesMufflerDevEnv/bin/activate", shell=True)
	except subprocess.CalledProcessError as e:
		print()
		print()
		print("Beginner Note: TesMufflerDevEnv was configured correctly using the 'source' command")
		print("Expert Note: source returned a non-zero exit status as expected \n\n")

	print("\n\nIf you would like to TURN OFF the TesMuffler Virtual Enviroment (BAD IDEA) run the 'deactivate' command\n\n")
	time.sleep(7)

    check_call("pip3 install can-isotp", shell=True)
	# Flask is the GUI frontend to that runs in parallel with python backend controling pumps
	# Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)
	# https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html	
	check_call("pip3 install flask", shell=True)

	# Tool For Style Guide Enforcement
	# https://flake8.pycqa.org/en/latest/
	check_call("pip3 install flake8", shell=True)


	check_call("pip3 install pyrebase", shell=True)

	# A simple Python Bluetooth interface to the BlueZ stack
	# https://github.com/ukBaz/python-bluezero
	check_call("sudo pip3 install bluezero", shell=True)

	# Allow the playing of .WAV or .MP3 files with pitch variance TODO SELECT 1 OF 3
	#TODO TEST https://simpleaudio.readthedocs.io/en/latest/capabilities.html
	check_call("sudo apt-get install -y python3-dev libasound2-dev", shell=True) 	# Only simpleaudio dependency
	check_call("pip install simpleaudio", shell=True)
	#TODO REMOVE IF SIMPLEAUDIO IS GOOD ENOUGH check_call("pip3 install samplerate", shell=True)
	#TODO REMOVE IF SAMPLERATE IS GOOD ENOUGH check_call("pip3 install pyaudio", shell=True)

	# Allow developer to download and convert to .WAV any car sound
	# Works on sites other then YouTube (with valid URL scheme)
	# https://youtube-dl.org/
	# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme
	check_call("pip3 install youtube-dl", shell=True)
	#TODO WHY DO I NEED TO INSTALL THIS ALSO??
	check_call("sudo apt install ffmpeg", shell=True)
	# Download the default engine sound
	print("DOWNLOADING: Two default ??6?? MB McLaren F1 engine sounds\n\n")
	time.sleep(5)
	#TODO check_call("youtube-dl -ci -f 'bestaudio[ext=wav]' http://www.youtube.com/watch?v=mOI8GWoMF4M", shell=True)
	#check_call("youtube-dl --extract-audio --audio-format wav http://www.youtube.com/watch?v=mOI8GWoMF4M", shell=True)
	check_call("youtube-dl --extract-audio --audio-format wav https://youtu.be/MmtdhnXsMqE", shell=True)
	check_call("cp *.wav McLarenF1.wav", shell=True)
	check_call("mv McLarenF1.wav ~/Tes/TesMuffler/Sounds", shell=True)
	check_call("youtube-dl --extract-audio --audio-format wav https://youtu.be/RjzC3-7H9NU", shell=True)
	check_call("cp *.wav McLarenF1StartUp.wav", shell=True)
	check_call("mv McLarenF1StartUp.wav ~/Tes/TesMuffler/Sounds", shell=True)
	check_call("rm *.wav", shell=True)

	if(hardware == PI_4):
		# Allow other computers to SSH into Pi running this code
		# Needed since SSH is not always installed on Pi distros
		check_call("sudo apt install openssh-server", shell=True)
		check_call("sudo apt install sshguard", shell=True)

		# Allow low level control on GPIO pins to drive RFID Readers, Servos, Motors, Relays, LEDs, etc
		# Python 3 install of GPIO and servo to match Flask
		# https://pypi.org/project/RPi.GPIO/
		check_call("pip3 install RPi.GPIO", shell=True)
		#TODO REMOVE IF RPi DOESNOT HAVE ENOUGH FEATURES check_call("sudo apt install python3-gpiozero", shell=True)
		#https://gpiozero.readthedocs.io/en/stable/installing.html

	elif(hardware == RP_2040):
		print("TODO")
		#https://pypi.org/project/energyusage/
		check_call("pip3 install energyusage", shell=True)

	elif(hardware == PI_PICO):
		print("TODO")
        elif(hardware == ISH_ALPINE_IPAD_OS):
               check_call("apk add py-pip")
               check_call("apk add git")
               check_call("apk add nano")

	elif(hardware == LINUX_PC): 

		# Install simple command line WAV audio player
		# Run 'play McLarenF1.wav' command to play sound
		# check_call("sudo apt install sox", shell=True)
		# https://github.com/scottrogowski/mongita
	    # https://www.w3schools.com/python/python_mysql_getstarted.asp
    	# https://itsfoss.com/install-mysql-ubuntu/
		check_call("sudo apt install mysql-server -y", shell=True)
		check_call("pip install mysql-connector-python", shell=True)

		# Start running mySQL server as root with sudo password
		#TODO FIGURE OUT PASSOWRD check_call("mysql -u root -p", shell=True)

	else:
		print("INVALID CLI ARGUMENTS: 'python3 install -d LinuxPC' is valid for example")

	print("\n\nRUN 'source TesMufflerDevEnv/bin/activate' command please...")

	#TODO COOL EXTRAS
	#https://www.builtinafrica.io/blog-post/vuyisile-ndlovu-pypi
	#https://docs.python.org/3/library/pathlib.html

	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)
