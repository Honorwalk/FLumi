

from appJar import gui
import functions
import variables
app=variables.variables.get(1)
milliGATAdd=variables.variables.get(2)
valcoAdd=variables.variables.get(3)
OMRONAdd=variables.variables.get(4)
def loadHome():

    app.addImage("logo","Images/logo220.png",0,0,25,5)
    app.zoomImage("logo",2)
    app.addIconButton("serialRefresh",lambda: functions.testConnection(),"connect-alt-1",1,22,2,2)


    app.addIconButton("milliGATButton",lambda: functions.switchPage(0),"arrow-1-up",6,3,4,2)
    app.addLabel("milliGATLabel","milliGAT Pump",6,8,6,1)
    app.addLabel("milliGATAddressText","Address: ",7,9,5,1)
    app.addOptionBox("milliGATAddress",["-select Address-",]+variables.connectedmilliGAT,7,14,1,1)
    app.setButtonBg("milliGATButton","darkGreen")
    
    app.addIconButton("valcoButton",lambda: functions.switchPage(1),"arrow-1-up",9,3,4,2)
    app.addLabel("valcoLabel","Valco Valve",9,8,6,1)
    app.addLabel("valcoAddressText","Address: ",10,9,5,1)
    app.addOptionBox("valcoAddress",["-select Address-",]+variables.connectedValco,10,14,1,1)
    app.setButtonBg("valcoButton","darkGreen")



    app.addIconButton("OMRONButton",lambda: functions.switchPage(2),"arrow-1-up",12,3,4,2)
    app.addLabel("OMRONLabel","OMRON Temp",12,8,6,1)
    app.addLabel("OMRONAddressText","Address: ",13,9,5,1)
    app.addOptionBox("OMRONAddress",["-select Address-",]+variables.connectedOMRON,13,14,1,1)
    app.setButtonBg("OMRONButton","darkGreen")
 
    app.getLabelWidget("valcoAddressText").config(font=15)
    app.getLabelWidget("milliGATAddressText").config(font=15)
    app.getLabelWidget("OMRONAddressText").config(font=15)
    app.getLabelWidget("valcoAddressText").config(font="ComicSans")

    
