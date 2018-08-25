from appJar import gui
import time
import serial
from string import ascii_uppercase
from . import variables
from . import valco
from . import OMRON
from . import Homescreen
import threading
app=variables.variables.get(1)
milliGATAdd=variables.variables.get(2)
valcoAdd=variables.variables.get(3)
OMRONAdd=variables.variables.get(4)

def press(btn):
		print(btn)

def spacer(x,y,ylen,xlen):
		app.addLabel("space"+str(variables.spacers),"",x,y,ylen,xlen)
		variables.spacers+=1


def homeScreen():
	app.selectFrame("Pages", 0, callFunction=True)
			
def switchPage(btn):

	app.selectFrame("Pages", btn, callFunction=True)

class mySerial():
	ser=""
	def error(self):
		app.errorBox("USB Not Connected","Device cannot open the serial port. Please make sure that the USB is securely plugged into a USB port and the device is powered on.", parent=None)
	def connect(self):
		self.connected=1
		try:
			self.ser = serial.Serial(
                    #port='COM5',
                    port='/dev/ttyUSB0',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=0.08
            )
		except serial.serialutil.SerialException:
			self.connected=0

	def disconnect(self):
		self.connected=0
		self.ser.close()

	def __init__(self):
		self.connect()
		self.disconnect()

	def testConnection(self):
		self.connect()
		if self.connected==1:
			def callback():
				variables.connectedmilliGAT=[]
				variables.connectedValco=[]
				variables.connectedOMRON=[]
				app.changeOptionBox("milliGATAddress",["-select Address-",]+variables.connectedmilliGAT)
				app.changeOptionBox("milliAddress",["-select Address-",]+variables.connectedmilliGAT)
				app.changeOptionBox("valcoAddress",["-select Address-",]+variables.connectedValco)
				app.changeOptionBox("OMRONAddress",["-select Address-",]+variables.connectedOMRON)

				app.disableButton("serialRefresh")
				app.disableButton("milliSerialRefresh")
				app.showImage("homeSpinner")
				app.showImage("milliSpinner")

				for char in ascii_uppercase:				
				#for milliGAT Pump
					self.ser.write((char+"PR EU\n").encode())
					self.ser.readline()
					mi=self.ser.readline()
					if mi!=b''and mi!=b'?\r\n':
						variables.connectedmilliGAT.append(char)
					elif mi==b'?\r\n':
						variables.connectedValco.append(char)
					self.ser.flushInput()
					self.ser.flushOutput()

				#for OMRON
				for char in range(0,9):
					string="@0"+str(char)+"RS01"
					string=string+getFCS(string)+"\r\n"
					self.ser.write((string).encode())
					om=self.ser.readline()
					if om!=b'':
							variables.connectedOMRON.append(char)
					self.ser.flushInput()
					self.ser.flushOutput()
				self.disconnect()
				app.changeOptionBox("milliGATAddress",["-select Address-",]+variables.connectedmilliGAT)
				app.changeOptionBox("milliAddress",["-select Address-",]+variables.connectedmilliGAT)
				app.changeOptionBox("valcoAddress",["-select Address-",]+variables.connectedValco)
				app.changeOptionBox("OMRONAddress",["-select Address-",]+variables.connectedOMRON)

				app.hideImage("homeSpinner")
				app.hideImage("milliSpinner")
				app.enableButton("serialRefresh") 
				app.enableButton("milliSerialRefresh")
				
			t=threading.Thread(target=callback, name="serialCheck")
			t.start() 

		else: self.error()
		
	def write(self,cmd):
		self.connect()
		if self.connected==1:
			self.ser.write(cmd)
			self.disconnect()
		else: self.error()

	def read(self):	
		self.connect()
		if self.connected==1:
			var=self.ser.read()
			self.disconnect()
			return var
		else: self.error()


def getFCS(command):
	binReturn=["0","0","0","0","0","0","0","0"]
	returner=0
	for char in command: 
		binChar="{0:08b}".format(ord(char))
		for j in range(0,8):
					if binReturn[j] == binChar[j]:
							binReturn[j]="0"
					else:
							binReturn[j]="1"

	returner=hex(int("".join(binReturn),2))[2:4]
	return returner.upper()+"*"




        
        
        





    
