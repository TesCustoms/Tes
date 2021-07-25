#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-07-17"
__doc__     = "Class to easily create 1000's of QR codes"
"""

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# Export cvs file to import into https://uqr.me/qr-code-generator
import cvs

try:
    # Generate .txt data logging and custom terminal debugging output
    from Debug import *

    #TODO

except ImportError:
	print("Debug didn't import correctly, please verify that Debug.py is in TODO")
	#TODO


class GenerateQRcode:

	def unitTest(extremeTest=false):
        print("STARTING GenerateQRcode.py Unit Test")
        
        TestObject1 = GenerateQRcode(1)

		TestObject2 = GenerateQRcode(100, 69)
		
		TestObject3 = GenerateQRcode(1000, "DOGE")
		
		if(extremeTest):
			customObjectType = TODO
			TestObject4 = GenerateQRcode(10000, customObjectType)
			
			TestObject5 = GenerateQRcode(100000)
			
			TestObject6 = GenerateQRcode(1000000)
			
	def __init__(self, numOfQrCodes=1, exampleDataTypeObject="420DOGE69XXX42ABC123"):
	"""
	
	Args:
		numOfQrCodes [INT]
		exampleDataTypeObject [Any Object] Defaults to string type if no constructor parameter given. Most program should pass a random UUID or URL to this constructor 
	Returns:
		A .cvs file for use with https://uqr.me/qr-code-generator TODO pyautogui the website for full automation 
	"""
		
		self.data = [exampleDataTypeObject] *  numOfQrCodes
		self.cvsFile = 

