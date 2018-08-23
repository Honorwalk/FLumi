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

def testConnection():
	app.disableButton("serialRefresh")
	app.showImage("spinner")

	def callback():
		variables.connectedmilliGAT=[]
		variables.connectedValco=[]
		variables.connectedOMRON=[]
		try:
			ser = serial.Serial(
					#port='COM5',
					port='/dev/ttyUSB0',
					baudrate=9600,
					parity=serial.PARITY_NONE,
					stopbits=serial.STOPBITS_ONE,
					bytesize=serial.EIGHTBITS,
					timeout=0.05
			)
			for char in ascii_uppercase:				
			#for milliGAT Pump
					ser.write((char+"PR EU\n").encode())
					ser.readline()
					mi=ser.readline()
					if mi!=b''and mi!=b'?\r\n':
							variables.connectedmilliGAT.append(char)
					ser.flushInput()
					ser.flushOutput()

			#for Valco Valve
					ser.write((char+"VT\n").encode())
					ser.readline()
					va=ser.readline()
					if va!=b''and va!=b'?\r\n':
							variables.connectedValco.append(char)
					ser.flushInput()
					ser.flushOutput()
			#for OMRON
			for char in range(0,9):
					string="@0"+str(char)+"RS01"
					string=string+getFCS(string)+"\r\n"
					ser.write((string).encode())
					om=ser.readline()
					if om!=b'':
							variables.connectedOMRON.append(char)
					ser.flushInput()
					ser.flushOutput()

			ser.close()
			app.changeOptionBox("milliGATAddress",["-select Address-",]+variables.connectedmilliGAT)
			app.changeOptionBox("milliAddress",["-select Address-",]+variables.connectedmilliGAT)
			app.changeOptionBox("valcoAddress",["-select Address-",]+variables.connectedValco)
			app.changeOptionBox("OMRONAddress",["-select Address-",]+variables.connectedOMRON) 
			
			

		except serial.serialutil.SerialException:
				app.errorBox("USB Not Connected","Device cannot open the serial port. Please make sure that the USB is securely plugged into a USB port and the device is powered on.", parent=None)
		app.hideImage("spinner")
		app.enableButton("serialRefresh")
	t=threading.Thread(target=callback, name="serialCheck")
	t.start()
	
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




        
        
        





    
