#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-07-17"
__doc__     = "Class to easily bulk create 1000's of QR codes"
"""

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

# Export csv file for import into https://uqr.me/qr-code-generator
# https://docs.python.org/3/library/csv.html
import csv

try:
    # Generate .txt data logging and custom terminal debugging output
    from Debug import *

    #TODO

except ImportError:
	print("Debug didn't import correctly, please verify that Debug.py is in TODO")
	#TODO


class GenerateQRcode:

	MAX_INT = 
	MAX_FLOAT =
	MAX_COMPLEX = 
	MAX_STRING_LENGTH = 1023
	UPPERCASE_A = 65
	LOWERCASE_Z = 122
	LOWER_NON_LETTER = 91
	UPPER_NON_LETTER = 96

	def unitTest(extremeTest=false):
        print("STARTING GenerateQRcode.py Unit Test")
        
        TestObject1 = GenerateQRcode(1)

		TestObject2 = GenerateQRcode(100, True, 69)
		
		TestObject3 = GenerateQRcode(1000, False, "DOGE")
		
		if(extremeTest):
			customObjectType = TODO
			TestObject4 = GenerateQRcode(10000, False, customObjectType)
			
			TestObject5 = GenerateQRcode(100000, True)
			
			TestObject6 = GenerateQRcode(1000000, True)
			
	def __init__(self, numOfQrCodes=1, randomData=True, exampleDataTypeObject="42DOGE69XXX420ABC123"):
	"""
	
	Args:
		numOfQrCodes [INT]
		exampleDataTypeObject [Any Object] Defaults to string type if no constructor parameter given. Most program should pass an integer, UUID string, or URL to this constructor 
	Returns:
		A .csv file for use with https://uqr.me/qr-code-generator TODO pyautogui the website for full automation 
	"""
		
		self.data = [exampleDataTypeObject] *  numOfQrCodes
		
		
		if(randomData):
			for i in range(0, numQrcodes):
				exampleData = type(exampleDataTypeObject)
				
				
				TODO
				random.seed()
				if(exampleData == 'int'):
					randomInt = randrange(0, MAX_INT)
				if(exampleData == 'float'):
					randomFloat = uniform(0, MAX_FLOAT)
				if(exampleData == 'str'):
					for i in range(0, MAX_STRING_LENGTH):
						# 6https://www.ascii-code.com/
						
						# Emulate a do-while loop in pyton
						while True:
						randomAsciiChar = randrange(UPPERCASE_A, LOWERCASE_Z) 
						 
						if(LOWER_NON_LETTER <= randomAsciiChar or randowAsciiChar <= UPPER_mulatebNON_LETTER): # [ / ] ^ _ ' 
						break 
					randomString += randomAsciiChar
							
				
				
				
				isString()
				isInt()
				isFloat()
				isObject()
				
				

		else:
			csvWriteHelper(exampleData)
			
		
		self.csvFile = QRcodeData.csv
		
		def csvWriteHelper():
			with open('QRcodeData.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            			quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([data] * 5 TODO)
		
		

