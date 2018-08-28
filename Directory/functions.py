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


def spacer(x,y,ylen,xlen):
		app.addLabel("space"+str(variables.spacers),"",x,y,ylen,xlen)
		variables.spacers+=1


def homeScreen():
	app.selectFrame("Pages", 0, callFunction=True)
			
def switchPage(btn):

	app.selectFrame("Pages", btn, callFunction=True)

class mySerial():
	ser=""
	paired=0
	def error(self):
		app.errorBox("USB Not Connected","Device cannot open the serial port. Please make sure that the USB is securely plugged into a USB port and the device is powered on.", parent=None)
		app.showImage("milliGATConnectN")
		app.showImage("valcoConnectN")
		app.showImage("OMRONConnectN")

		app.hideImage("milliGATConnectY")
		app.hideImage("valcoConnectY")
		app.hideImage("OMRONConnectY")

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
		if self.ser!="":
			self.ser.close()

	def __init__(self):
		self.connect()
		self.disconnect()
		
	def testConnection(self,obj,typ):
		obj.address.load()
		self.connect()
		if self.connected==1:
			def callback():
				self.paired=1
			
				app.disableButton("serialRefresh")
				app.disableButton("milliSerialRefresh")
				app.showImage("homeSpinner")
				app.showImage("milliSpinner")
				prev=self.testInitAddr(obj.address)

				#for milliGAT Pump 
				if typ==0 or typ==1:
					if prev[0]==0 or obj.address.milliGAT==[]:
						obj.address.milliGAT=[]
						for char in ascii_uppercase:	
							self.write((char+"PR EU\n"))
							self.read()
							mi=self.read()
							if mi!=b''and mi!=b'?\r\n':
								obj.address.milliGAT.append(char)
							self.ser.flushInput()
							self.ser.flushOutput()
					obj.address.milliGATSettings=[]
					for addr in obj.address.milliGAT:
						self.write(str(addr)+"PR EU\n")
						self.read()
						eu=int(self.read())
						bl=0
						obj.address.milliGATSettings.append(tuple((eu,bl)))
						obj.address.save()
					print(obj.address.milliGATSettings)

					if len(obj.address.milliGAT)!=0:
						app.showImage("milliGATConnectY")
						app.hideImage("milliGATConnectN")
					else: 
						app.showImage("milliGATConnectN")
						app.hideImage("milliGATConnectY")

				#for valco Valve
				if typ==0 or typ==2:
					if prev[1]==0 or obj.address.valco==[]:
						obj.address.valco=[]
						for char in ascii_uppercase:	
							self.write((char+"PR OP\n"))
							self.read()
							mi=self.read()
							if mi!=b''and mi!=b'?\r\n':
								obj.address.valco.append(char)
							self.ser.flushInput()
							self.ser.flushOutput()
					if len(obj.address.valco)!=0:
						app.showImage("valcoConnectY")
						app.hideImage("valcoConnectN")
					else:
						app.showImage("valcoConnectN")
						app.hideImage("valcoConnectY")
						
				#for OMRON
				if typ==0 or typ==3:
					if prev[2]==0 or obj.address.OMRON==[]:
						obj.address.OMRON=[]
						for char in range(0,9):
							string="@0"+str(char)+"RS01"
							string=string+getFCS(string)+"\r\n"
							self.write((string))
							om=self.read()
							if om!=b'':
									obj.address.OMRON.append(char)
							self.ser.flushInput()
							self.ser.flushOutput()

					if len(obj.address.OMRON)!=0:
						app.showImage("OMRONConnectY")
						app.hideImage("OMRONConnectN")
					else: 
						app.showImage("OMRONConnectN")
						app.hideImage("OMRONConnectY")
				self.disconnect()
				
				app.changeOptionBox("milliAddress",["-select Address-",]+obj.address.milliGAT)
				app.setOptionBox("milliAddress",1)
				#app.changeOptionBox("valcoAddress",["-select Address-",]+obj.address.valco)
				#app.setOptionBox("valcoAddress",1)
				#app.changeOptionBox("OMRONAddress",["-select Address-",]+obj.address.OMRON)
				#app.setOptionBox("OMRONAddress",1)

				
				


				app.hideImage("homeSpinner")
				app.hideImage("milliSpinner")
				app.enableButton("serialRefresh") 
				app.enableButton("milliSerialRefresh")
				obj.address.save()
				

			t=threading.Thread(target=callback, name="serialCheck")
			t.start() 

		else: self.error()
	
	def testInitAddr(self,address):
		test=[1,1,1]
		for addr in address.milliGAT:
			self.write((addr+"PR EU\n"))
			self.read()
			mi=self.read()
			if mi==b''or mi==b'?\r\n':
				test[0]=0
			self.ser.flushInput()
			self.ser.flushOutput()

		for addr in address.valco:
			self.write((addr+"PR OP\n"))
			self.read()
			va=self.read()
			if va==b''or va==b'?\r\n':
				test[1]=0
			self.ser.flushInput()
			self.ser.flushOutput()

		for addr in address.OMRON:
			string="@0"+str(addr)+"RS01"
			string=string+getFCS(string)+"\r\n"
			self.ser.write((string).encode())
			om=self.ser.readline()
			if om==b'':
				test[2]=0
			self.ser.flushInput()
			self.ser.flushOutput()

		if address.milliGAT==[]:test[0]=0
		if address.valco==[]:test[1]=0
		if address.OMRON==[]:test[2]=0
		return test

	def write(self,cmd):
		cmd=cmd.encode()
		if self.connected==1:
			self.ser.write(cmd)
		else: self.error()

	def read(self):	
		if self.connected==1:
			var=self.ser.readline()
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




        
        
        





    
