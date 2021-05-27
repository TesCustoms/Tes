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

# Allow install to pause, allowing programmer to read terminal output
# https://docs.python.org/3/library/time.html
import time

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call


if __name__ == "__main__":

	parser = argparse.ArgumentParser(prog = "TesMuffler install script", description = __doc__, add_help=True)
	parser.add_argument("-d", "--device", type=str, default= PI_4, choices=[PI_4, RP2040, PI_PICO], help="Select the hardware code is running on">
	#TODO Add to TesMufflerDriver.py - parser.add_argument("-t", "--trace", type=int, default=0, help="Program trace level.")
	args = parser.parse_args()

	hardware = args.device

	check_call("clear",shell=True)  	# Clear terminal
	print("Starting TesMuffler install")
	time.sleep(2)				# Pause 2 seconds

	# Check and update your system
	check_call("sudo apt update", shell=True)
	check_call("sudo apt upgrade", shell=True)

	# Install PIP3 to stay away from all things Python 2!
	check_call("sudo apt install python-pip3", shell=True)

	# Start autoconfiguring a virtual enviroment like a good programmer should :)
	# https://www.geeksforgeeks.org/python-virtual-environment/
	check_call("pip3 install virtualenv", shell=True)
	check_call("virtualenv --version", shell=True)
	time.sleep(2)
	check_call("virtualenv TesMufflerDevEnv", shell=True)
	# Specifiy Python 3 interpreter to stay away from all things Python 2!
	check_call("virtualenv -p /usr/bin/python3 virtualenv_name", shell=True)
	

check_call("", shell=True)

source virtualenv_name/bin/activate
	#TODO COOL EXTRAS
	#pipenv
	#https://pypi.org/project/energyusage/
	#https://github.com/scottrogowski/mongita
	#https://www.builtinafrica.io/blog-post/vuyisile-ndlovu-pypi
	#https://docs.python.org/3/library/pathlib.html

	# Allow other computers to SSH into Pi running this code
	# Needed since SSH is not always installed on Pi distros
	check_call("sudo apt install openssh-server", shell=True)
	check_call("sudo apt install sshguard", shell=True)

    # https://www.w3schools.com/python/python_mysql_getstarted.asp
    # https://itsfoss.com/install-mysql-ubuntu/
    check_call("sudo apt install mysql-server -y", shell=True)
    check_call("pip install mysql-connector-python", shell=True)

    # Start running mySQL server as root with sudo password
    check_call("mysql -u root -p", shell=True)




	# Flask requires Python 3 to work
	check_call("sudo apt install python3-pip", shell=True)


	# evdev required to setup RFID Reader
	check_call("pip install evdev", shell=True)

	# Flask is the GUI frontend to that runs in parallel with python backend controling pumps
	# Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)
	# https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html
	check_call("pip3 install flask", shell=True)

    #TODO pip3 install samplerate

	# Low level control on GPIO pins to drive RFID Readers, Servos, Motors, Relays, LEDs, etc
	# Python 3 install of GPIO and servo to match Flask
	# https://gpiozero.readthedocs.io/en/stable/installing.html
	# https://pypi.org/project/RPi.GPIO/
	if(CONFIG == "Pi3B+"):
		check_call("sudo apt install python3-gpiozero", shell=True)
		check_call("pip install RPi.GPIO", shell=True) #Used for RFID Reader
	elif(CONFIG == "UbuntuOnWindows"):
		check_call("sudo pip install gpiozero", shell=True)
	elif(CONFIG == "UbuntuMate"):
		print("TODO")
		#TODO TEST check_call("sudo pip install gpiozero", shell=True)
	elif(CONFIG == "Alpine"):
		print("TODO")
		#TODO TEST check_call("sudo apt install python3-gpiozero", shell=True)
	else:
		print("INVALID CONFIG SELECTED")

	#IF GPIO ZERO &  RPi.GPIO FAIL OR ARE NOT POWERFUL ENOUG
	#check_call("sudo pip3 install adafruit-circuitpython-motorkit", shell=True)
