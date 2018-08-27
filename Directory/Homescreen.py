

from appJar import gui
from . import functions
from . import variables
app=variables.variables.get(1)
milliGATAdd=variables.variables.get(2)
valcoAdd=variables.variables.get(3)
OMRONAdd=variables.variables.get(4)
def loadHome():
    serial=functions.mySerial()
    address=variables.address(serial)
    with app.frame("homeTitleBar"):
        app.setPadding([5,5])
        app.addImage("logo","Directory/Images/logo600.gif",0,1,6,2)
        app.addIconButton("exitButton",lambda: app.stop(), "exit",0,0,1,1)
        app.setButtonBg("exitButton","red")
        app.addIconButton("serialRefresh",lambda: serial.testConnection(address),"connect-alt-1",0,7,1,1)
        app.setButtonBg("serialRefresh","lightGrey")
        app.addImage("homeSpinner","Directory/Images/loading.gif",0,7,1,1)
        functions.spacer(1,7,1,1)
        app.setImageBg("homeSpinner","lightGrey")
        app.setAnimationSpeed("homeSpinner",60)
        app.hideImage("homeSpinner")



    with app.frame("homeMain"):
        app.setPadding([10,10])
        
        app.addIconButton("milliGATButton",lambda: functions.switchPage(1),"arrow-1-up",4,1,1,2)
        app.addLabel("milliGATLabel","milliGAT Pump",4,2,1,1)
        app.addIcon("milliGATConnectY","connect",5,2,1,1)
        app.addIcon("milliGATConnectN","connection-error",5,2,1,1)
        app.setImageSticky("milliGATConnectN","nse")
        app.setImageSticky("milliGATConnectY","nse")
        app.hideImage("milliGATConnectY")
        app.setButtonBg("milliGATButton","green")

        app.addIconButton("valcoButton",lambda: functions.switchPage(2),"arrow-1-up",7,1,1,2)
        app.addLabel("valcoLabel","Valco Valve",7,2,2,1)
        app.addIcon("valcoConnectY","connect",8,2,1,1)
        app.addIcon("valcoConnectN","connection-error",8,2,1,1)
        app.setImageSticky("valcoConnectN","nse")
        app.setImageSticky("valcoConnectY","nse")
        app.hideImage("valcoConnectY")
        app.setButtonBg("valcoButton","green")

        app.addIconButton("OMRONButton",lambda: functions.switchPage(3),"arrow-1-up",10,1,1,2)
        app.addLabel("OMRONLabel","OMRON Temp",10,2,2,1)
        app.addIcon("OMRONConnectY","connect",11,2,1,1)
        app.addIcon("OMRONConnectN","connection-error",11,2,1,1)
        app.setImageSticky("OMRONConnectN","nse")
        app.setImageSticky("OMRONConnectY","nse")
        app.hideImage("OMRONConnectY")
        app.setButtonBg("OMRONButton","green")



    

    
