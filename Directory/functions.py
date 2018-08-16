from appJar import gui
import milliGAT
import time
import serial
from string import ascii_uppercase
import variables
app=variables.variables.get(1)
milliGATAdd=variables.variables.get(2)
valcoAdd=variables.variables.get(3)
OMRONAdd=variables.variables.get(4)

def press(btn):
        print(btn)


def layout():
        for x in range(25):
                app.addLabel(str(variables.layouts)+"side%s"%(x),"",0,x)
        for y in range(1,15):
                app.addLabel(str(variables.layouts)+"top%s"%(y),"",y,0)
        variables.layouts+=1

def switchPage(btn):
        app.selectFrame("Pages",1,callFunction=True)
        app.selectFrame("Control",btn,callFunction=True)
def loadMenu():
        app.addIconButton("HomeButton",lambda: app.selectFrame("Pages",0,callFunction=True),"arrow-1-up",6,3,4,2)
def testConnection():
        variables.connectedmilliGAT=[]
        variables.connectedValco=[]
        variables.connectedOMRON=[]
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
                ser.flushInput()
                ser.flushOutput()

        #for Valco Valve
                ser.write((char+"VT\n").encode())
                ser.readline()
                va=ser.readline()
                if mi!=b''and mi!=b'?\r\n':
                        variables.connectedmilliGAT.append(char)
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
        app.changeOptionBox("valcoAddress",["-select Address-",]+variables.connectedValco)
        app.changeOptionBox("OMRONAddress",["-select Address-",]+variables.connectedOMRON)


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





                       
    

        
        
        





    
