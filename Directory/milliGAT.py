from appJar import gui
from . import functions
from . import Homescreen
from . import variables
from . import numPadInit
import time
app=variables.variables.get(1)
milliGATAdd=variables.variables.get(2)
valcoAdd=variables.variables.get(3)
OMRONAdd=variables.variables.get(4)
volume=0
flowRate=0

class milliGATHome():
        milliVar=variables.milliGAT()
        def __init__(self):
                with app.frame("controlPage"): 
                        app.addIconButton("milliExitButton",lambda: app.stop(), "exit",0,0,1,1)
                        app.addLabel("milliMenuTitle","millIGAT Pump Control",0,2,1,1)
                        app.getLabelWidget("milliMenuTitle").config(font="20")
                        app.setButtonBg("milliExitButton","red")
                        with app.frame("milliRightButtions",0,4,1,1):
                                app.addIconButton("milliHomeButton",lambda: functions.homeScreen(),"arrow-1-left",0,0) 
                                app.addIconButton("milliSerialRefresh",functions.testConnection,"connect-alt-1",1,0)
                        functions.spacer(0,1,1,1)
                        functions.spacer(0,3,1,1)

                
                with app.tabbedFrame("milliGUI"): 
                        with app.tab("Home"):
                                with app.frame("milliLeft",0,0):
                                        with app.frame("milliAspirate"):
                                                app.addIconButton("leftAspirate",lambda: aspirate("left"),"arrow-1-left",0,0)
                                                app.addIconButton("stopAspirate",lambda: aspirate("stop"),"stop-alt",0,1)
                                                app.addIconButton("rightAspirate",lambda: aspirate("right"),"arrow-1-right",0,2)
                                                app.setButtonFg("leftAspirate","green")

                                        with app.frame("milliImage"):
                                                app.addImage("milliGATImage","Directory/Images/milliGAT.png",0,0)
                                                app.addIcon("leftFlow","arrow-1-left",1,0)
                                                app.addIcon("rightFlow","arrow-1-right",1,0)
                                                app.addIcon("stopFlow","stop-alt",1,0)
                                                app.hideImage("leftFlow")
                                                app.hideImage("rightFlow")

                                        with app.frame("milliSlew"):
                                                app.addIconButton("leftSlew",lambda: slew("left"),"arrow-1-backward",0,0)
                                                app.addIconButton("stopSlew",lambda: slew("stop"),"stop-alt",0,1)
                                                app.addIconButton("rightSlew",lambda: slew("right"),"arrow-1-forward",0,2)
                                with app.frame("milliRight",0,1):
                                        app.addLabel("milliAddressText","Pump Address: ",0,0)
                                        app.addOptionBox("milliAddress",["-select Address-",]+variables.connectedmilliGAT,0,1,2)
                                        app.setOptionBoxSticky("milliAddress","we")
                                        app.addLabel("milliVolumeText1","Volume: ",1,0)
                                        app.addNamedButton(str(self.milliVar.volume),"milliVolume",lambda btn: numPadInit.pad.show(5,0,btn,self),1,1)
                                        app.getButtonWidget("milliVolume").config(font="20")
                                        app.addLabel("milliVolumeText2","µl",1,2)
               
                                        app.addLabel("milliFlowRateText","FlowRate: ",2,0)
                                        app.addNamedButton(str(self.milliVar.flowRate),"milliFlowRate",lambda btn: numPadInit.pad.show(5,0,btn,self) ,2,1)
                                        app.getButtonWidget("milliFlowRate").config(font="20")
                                        app.addLabel("milliFlowRateText2","µl/sec",2,2)





                        with app.tab("Settings"):
                                app.addIconButton("milExitButton",lambda: app.stop(), "exit",)


def aspirate(direction):
        items=["rightAspirate","leftAspirate","rightSlew","leftSlew","stopSlew"]
        if direction=="left":
                app.hideImage("stopFlow")
                app.showImage("leftFlow")
                for i in items:
                        app.disableButton(i)
        elif direction=="right":
                app.hideImage("stopFlow")
                app.showImage("rightFlow")
                for i in items:
                        app.disableButton(i)
        elif direction=="stop":
                app.hideImage("rightFlow")
                app.hideImage("leftFlow")
                app.showImage("stopFlow")
                for i in items:
                        app.enableButton(i)

def slew(direction):
        items=["rightAspirate","leftAspirate","rightSlew","leftSlew","stopAspirate"]
        if direction=="left":
                app.hideImage("stopFlow")
                app.showImage("leftFlow")
                for i in items:
                        app.disableButton(i)
        elif direction=="right":
                app.hideImage("stopFlow")
                app.showImage("rightFlow")
                for i in items:
                        app.disableButton(i)
        elif direction=="stop":
                app.hideImage("rightFlow")
                app.hideImage("leftFlow")
                app.showImage("stopFlow")
                for i in items:
                        app.enableButton(i)

def getVolume():
        print("getVolume")
def getFlowRate():
        print("getFlowRate")


                







