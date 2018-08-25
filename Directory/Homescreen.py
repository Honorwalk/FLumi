

from appJar import gui
from . import functions
from . import variables
app=variables.variables.get(1)
milliGATAdd=variables.variables.get(2)
valcoAdd=variables.variables.get(3)
OMRONAdd=variables.variables.get(4)
def loadHome():
    serial=functions.mySerial()
    app.addImage("logo","Directory/Images/logo600.gif",0,1,6,2)
    app.addIconButton("exitButton",lambda: app.stop(), "exit",0,0,1,1)
    app.setButtonBg("exitButton","red")
    app.addIconButton("serialRefresh",serial.testConnection,"connect-alt-1",0,7,1,1)
    app.setButtonBg("serialRefresh","lightGrey")
    app.addImage("homeSpinner","Directory/Images/loading.gif",1,7,1,1)
    app.setAnimationSpeed("homeSpinner",60)
    app.hideImage("homeSpinner")



    functions.spacer(1,0,1,1)
    functions.spacer(2,0,7,1)
    
    app.addIconButton("milliGATButton",lambda: functions.switchPage(1),"arrow-1-up",4,1,1,2)
    app.addLabel("milliGATLabel","milliGAT Pump",4,2,2,1)
    app.addLabel("milliGATAddressText","Address: ",5,2,1,1)
    app.addOptionBox("milliGATAddress",["-select Address-",]+variables.connectedmilliGAT,5,3,1,1)
    app.setButtonBg("milliGATButton","darkGreen")
    functions.spacer(6,0,7,1)

    app.addIconButton("valcoButton",lambda: functions.switchPage(2),"arrow-1-up",7,1,1,2)
    app.addLabel("valcoLabel","Valco Valve",7,2,2,1)
    app.addLabel("valcoAddressText","Address: ",8,2,1,1)
    app.addOptionBox("valcoAddress",["-select Address-",]+variables.connectedValco,8,3,1,1)
    app.setButtonBg("valcoButton","darkGreen")
    functions.spacer(9,0,7,1)

    
    app.addIconButton("OMRONButton",lambda: functions.switchPage(3),"arrow-1-up",10,1,1,2)
    app.addLabel("OMRONLabel","OMRON Temp",10,2,2,1)
    app.addLabel("OMRONAddressText","Address: ",11,2,1,1)
    app.addOptionBox("OMRONAddress",["-select Address-",]+variables.connectedOMRON,11,3,1,1)
    app.setButtonBg("OMRONButton","darkGreen")
    functions.spacer(12,0,7,1)


    app.getLabelWidget("valcoAddressText").config(font=15)
    app.getLabelWidget("milliGATAddressText").config(font=15)
    app.getLabelWidget("OMRONAddressText").config(font=15)
    

    
