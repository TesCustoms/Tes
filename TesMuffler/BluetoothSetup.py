#!/usr/bin/env python3

"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-07-31"
__doc__     = "Class to automate bluetooth pairing of hardware & mobile app to any Tesla vehicle"  # NOQA: E501
"""
TODO = -1  #REMOVE ONCE IN PRODUCTION AND NOQA: E402 WILL GO AWAY :)

# Allow Linux, MacOS, ESP-32 CPUs to access host machine Bluetooth resources
# https://pypi.org/project/PyBluez/
#import bluetooth
# https://ukbaz.github.io/howto/ubit_workshop.html
from bluezero import * #TODO WHAT TPYE OF DEVICES SHOULD I IMPORT

# Create unique random ID for each vehicle for user privacy
# https://docs.python.org/3/library/uuid.html
import uuid

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

try:
    # Generate .txt debug logs and custom terminal debugging print statement
    from Debug import Debug, Dprint, Lprint
    #TODO

except ImportError:
    print("Debug didn't import correctly, "
          "please verify that Debug.py is in directory of BluetoothSetup.py")
    #TODO


class BluetoothSetup:

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

    # Bluetooth class type CONSTANTS
    TELSA_BLUETOOTH_CLASS = TODO
    CELLPHONE_BLUETOOTH_CLASS = TODO
    HEADPHONE_BLUETOOTH_CLASS = TODO

    # Debugging CONSTANTS
    DEBUG_STATEMENTS_ON = True

    def __init__(self, model=ALL):
        """Construcor to find & connnect to the strongest Tesla Bluetooth signal

        Args:
            model (char, optional): Selection filter to limit the car models
            that bluetooth will atttempt to pair and connect to

        Returns:
            Newly created BluetoothSetup() object
        """

        thisCodesFilename = os.path.basename(__file__)
        self.DebugObject = Debug(BluetoothSetup.DEBUG_STATEMENTS_ON,
                                 thisCodesFilename)

        # https://www.w3schools.com/python/python_lists_methods.asp
        id = uuid.uuid4()
        self.deviceIdList = [id]

        bluetoothDevices = findDevices(model)
        numOfDevices = len(bluetoothDevices)
        for i in range(0, numOfDevices):
            newId = uuid4()
            self.deviceIdList.append(newId)

        # Connect to the strongest bluetooth signal after 42 second search
        for j in range(0, numOfDevices):
            if(bluetoothDevices.lookup_name(TODO, 42) == "Tesla"):
                self.DebugObject.Dprint("TODO")

        for listIndex in range(0, numOfDevices):
            for tupleIndex in range(0, 3):
                if(bluetoothDevices[listIndex][tupleIndex] == BluetoothSetup.TESLA_BLUETOOTH_CLASS):  # NOQA: E501
                    # pairWithVehicle()
                    self.connectedCar = TODO #connectToVehicle(bluetoothDevice[listIndex][tupleIndex])
                    self.carToConnected = Car.Tesla(adapter_addr='xx:xx:xx:xx:xx:xx',
                                                    device_addr='yy:yy:yy:yy:yy:yy')
                    self.carToConnected.connect()

        def unitTest():
            """Test connecting ESP-32 to a Tesla Cybertruck

            Args:
                NONE

            Returns:
                NOTHING
            """

            TestObject1 = BluetoothSetup('C')
            TestObject1.DebugObject.Dprint("TesMuffler OBD Module connected to Cybertruck")  # NOQA: E501
            TestObject1.disconnectFromVehicle()

        def findDevices(self):
            """Search for ANY nearby device with a strong Bluetooth signal

            Args:
                NONE

            Returns:
                A Tuple (address, human reable name, bluetooth class type TODO)
                of all bluetooth devices within range #TODO(~100 meters)
            """

            nearbyDevices = bluetooth.discover_devices(lookup_names=True,
                                                       lookup_class=True)

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
        BluetoothSetup.unitTest()
    except AssertionError as error:
        print("BluetoothSetup Unit Test failed: {0} ".format(error))
    except NameError as error:
        print("BluetoothSetup Unit Test failed: {0} ".format(error))

    print("END of BluetoothSetup.py MAIN method")
