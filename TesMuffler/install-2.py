#!/usr/bin/env python3
"""
__author__ =  "Blaze Sanders"
__email__ =   "blaze.d.a.sanders@gmail.com"
__company__ = "Humanity"
__status__ =  "Development"
__date__ =    "Late Updated: 2021-05-27"
__doc__ =     "Setup a TesMuffler dev enviroment using VirtualEnv"
"""


# Hardware that code can run on CONSTANTS
PI_4    = "Raspberry Pi 4"
RP_2040 = "Arduino Microcontroller"
PI_PICO = "Raspbery Pi Microntroller"


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

	parser = argparse.ArgumentParser(prog = "TesMuffler install script", description = __doc__, add_help=True)
	parser.add_argument("-d", "--device", type=str, default= PI_4, choices=[PI_4, RP_2040, PI_PICO], help="Select the hardware code is running on")
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


	# Install PIP3 to stay away from all things Python 2!
	# Also Flask GUI's (TODO FUTURE WORK) require Python 3 or above
	check_call("sudo apt install python3-pip", shell=True)


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
		check_call("source TesMufflerDevEnv/bin/activate", shell=True)
	except subprocess.CalledProcessError as e:
		print()
		print()
		print("Beginner: TesMufflerDevEnv was configured correctly using the 'source' command")
		print("Expert: source returned a non-zero exit status as expected")
		print()
		print()
	print("If you would like to TURN OFF the TesMuffler Virtual Enviroment (BAD IDEA) run the 'deactivate' command")
	time.sleep(7)

	# Flask is the GUI frontend to that runs in parallel with python backend controling pumps
	# Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)
	# https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html
	check_call("pip3 install flask", shell=True)

	# Allow the playing of .WAV or .MP3 files with pitch variance TODO SLECT 1 OF 3
	check_call("pip install simpleaudio", shell=True)
	#TODO REMOVE IF NOT NEEDED check_call("pip3 install samplerate", shell=True)
	#TODO REMOVE IF NOT NEEDED check_call("pip3 install pyaudio", shell=True)


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

	elif(hardware == PI_PICO):
		print("TODO")

	elif(hardware == LINUX_PC):
		# https://github.com/scottrogowski/mongita
	    	# https://www.w3schools.com/python/python_mysql_getstarted.asp
    		# https://itsfoss.com/install-mysql-ubuntu/
		check_call("sudo apt install mysql-server -y", shell=True)
		check_call("pip install mysql-connector-python", shell=True)

		# Start running mySQL server as root with sudo password
		check_call("mysql -u root -p", shell=True)

	else:
		print("INVALID CLI ARGUMENTS: 'install -d PI_4' is valid for example")

	#TODO COOL EXTRAS
	#https://pypi.org/project/energyusage/
	#https://www.builtinafrica.io/blog-post/vuyisile-ndlovu-pypi
	#https://docs.python.org/3/library/pathlib.html

	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)










