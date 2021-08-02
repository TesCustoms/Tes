#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-02"
__doc__     = "Class to create 1000's of QR codes with random data"
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
	from  
	#TODO

except ImportError:
	print("Debug didn't import correctly, please verify that Debug.py is in TODO")
	#TODO

# REMOVE ONCE CODE IS IN PRODUCTION
TODO = -1

class GenerateQRcode:
	"""Generate QR code .png and .csv 
	
		Normal use case for this class is to create a .cvs file for use with https://uqr.me/qr-code-generator 
		
		TODO pyautogui the website https://uqr.me for full automation 
	"""
	
	MAX_INT = 
	MAX_FLOAT =
	MAX_COMPLEX = 
	MAX_STRING_LENGTH = 1023
	UPPERCASE_A = 65
	LOWERCASE_Z = 122
	LOWER_NON_LETTER = 91
	UPPER_NON_LETTER = 96

	DEBUG_STATEMENTS_ON = True

	def unitTest(extremeTest=False):
		print("STARTING GenerateQRcode.py Unit Test")
		
		TestObject1 = GenerateQRcode(1)
		TestObject2 = GenerateQRcode(100, 69)
		TestObject3 = GenerateQRcode(1000, "DOGE")
		
		if(extremeTest):
			# Person() is 
			customObjectType = Person("Blaze", 5318008, 18) 
			
			TestObject4 = GenerateQRcode(10000, customObjectType)
			TestObject5 = GenerateQRcode(100000)
			TestObject6 = GenerateQRcode(1000000)
			
		print("ENDING GenerateQRcode.py Unit Test")


	def __init__(self, numOfQrCodes=1, exampleDataTypeObject="420DOGE69XXX42ABC123"):
		"""Constructor to initialize an GenerateQRcode object
		
		Defaults to one QR code with embedded string data
			
		Args:
			numOfQrCodes [INT] Number of QR code(s) configurations store within the .csv file instance variable
			exampleDataTypeObject [Any Object]
			 Defaults to string type if no constructor parameter given. Most program should pass a random UUID or URL to this constructor 

	    Instance variables:
	    	DebugObject [Debug.py Object] Useful for debugging & data logging
	                                                                                                           
		Returns:
           New GenerateQRcode() object
		"""
		
		thisCodesFilename = os.path.basename(__file__)
		self.DebugObject = Debug(GenerateQRcode.DEBUG_STATEMENTS_ON, thisCodesFilename)
		
		self.data = [exampleDataTypeObject] *  numOfQrCodes
		return self.csvFile
		
		if(randomData):
			for i in range(0, numQrcodes):
				exampleData = type(exampleDataTypeObject)
				
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

		return self.csvFile
				
		def csvWriteHelper():
			with open('QRcodeData.csv', 'w', newline='') as csvfile:
    			spamwriter = csv.writer(csvfile, delimiter=' ',
                            			quotechar='|', quoting=csv.QUOTE_MINIMAL)
    		spamwriter.writerow([data] * 5 TODO)
		
if __name__ == "__main__":

	try:
		GenerateQRcode.unitTest()
	except AssertionError as error: #NameError:
		print("Generate QR Code Unit Test failed :(")
		
	print("END of GenerateQRcode.py MAIN method")
