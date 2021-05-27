#!/usr/bin/env python
"""
__author__ =  "Blaze Sanders"
__email__ =   "blaze.d.a.sanders@gmail.com"
__company__ = "Humanity"
__status__ =  "Development"
__date__ =    "Late Updated: 2021-04-27"
__doc__ =     "Install script to setup TesMuffler dev enviroment"
"""

CONFIG = "Pi3B+" # or "UnbuntuOnWindows" of "UbuntuMate" or "Alpine"

# Allow BASH commands to be run inside python code like this file
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

if __name__ == "__main__":
	check_call("clear",shell=True)  # Clear terminal

	# Check and update your system
	check_call("sudo apt update", shell=True)
	check_call("sudo apt upgrade", shell=True)
	
	python-pip3
	pipenv
	https://pypi.org/project/energyusage/
	
	https://github.com/scottrogowski/mongita
	
	https://www.builtinafrica.io/blog-post/vuyisile-ndlovu-pypi
	
	https://docs.python.org/3/library/pathlib.html

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
