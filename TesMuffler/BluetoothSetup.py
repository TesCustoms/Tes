#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-07-18"
__doc__     = "Class to automate bluetooth pairing of hardware & mobile app to any Tesla vehicle"
"""

# Allow Pi, Linux MacOS, and Windows CPUs to access host machine Bluetooth resources
# https://pypi.org/project/PyBluez/
import bluetooth

# Create unique random ID for each vehicle for user privacy
#https://docs.python.org/3/library/uuid.html
import uuid

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

try:
    # Generate .txt data logging and custom terminal debugging output
    from Debug import *

    #TODO

except ImportError:
    print("Debug didn't import correctly, please verify that Debug.py is in directory of BluetoothSetup.py")
    #TODO


class BluetoothSetup:

	TODO = -1

	# Model model name CONTSTANTS
	MODEL_S = 'S'
	MODEL_3 = '3'
	MODEL_X = 'X'
	MODEL_Y = 'Y'
	CYBER_TRUCK = 'C'
	ATV = 'A'
	ROADSTER_V2 = 'R'
	SEMI_TRUCK = 'S'
	ALL = 'S3XY CARS'

	# Bluetooth clas type CONSTANTS
	TELSA_BLUETOOTH_CLASS = TODO
	CELLPHONE_BLUETOOTH_CLASS = TODO
	HEADPHONE_BLUETOOTH_CLASS = TODO

	# Debugging CONSTANTS
	DEBUG_STATEMENTS_ON = True


	def __init__(self, model=ALL):
		"""
		Args:
			model [CHAR] Optional filter to TODO
		"""
		thisCodesFilename = os.path.basename(__file__)
		self.DebugObject = Debug(BlueboothSetup.DEBUG_STATEMENTS_ON, thisCodesFilename)

		# https://www.w3schools.com/python/python_lists_methods.asp
		id = uuid4()
		self.deviceIdList = [id]

		bluetoothDevices = findDevices(model)
		numOfDevices = len(bluetoothDevices)
		for i in range(0, numOfDevices):
			newId = uuid4()
			self.deviceIdList.append(newId)

		#Strongest bluetooth signal afte search for 42 seconds
		for j in range(0,numOfDevices):
			if(bluetoothDevices.lookup_name(TODO, 42) == "Tesla")

			if(bluetoothDevices[listIndex][tupleIndex] == BluetoothSetup.TESLA_BLUETOOTH_CLASS):
				# pairWithVehicle()
				self.connectedCar = TODO #connectToVehicle()



	def unitTest():
		TestObject1 = BluetoothSetup('C')

		TestObject1.disconnectFromVehicle()


	def findDevices(self):
		"""Search for ANY nearby device with a strong Bluetooth signal

		Args:
			NONE

		Returns:
			Tuple (address, human reable name, bluetooth class type TODO) of bluetooth devices within range
		"""
		nearbyDevices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)

		return nearbyDevices


	def pairWithVehicle():
		"""TODO
		"""
		print("TODO")

	def connectToVehicle():
		"""TODO
		"""
		print("TODO")


	def disconnectFromVehicle():
		"""TODO
		"""
		print("TODO")


if __name__ == "__main__":

	try:
		Bluetoothsetup.unitTest()
	except AssertionError as error: #NameError:
		print("BluetoothSetup Unit Test failed :(")

	print("END of BluetoothSetup.py MAIN method")
