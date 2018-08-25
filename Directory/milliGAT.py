from appJar import gui
from . import functions
from . import Homescreen
from . import variables
from . import numPadInit
import serial
import time
app=variables.variables.get(1)
milliGATAdd=variables.variables.get(2)
valcoAdd=variables.variables.get(3)
OMRONAdd=variables.variables.get(4)
volume=0
flowRate=0

class milliGATHome():
        milliVar=variables.milliGAT()
        serial=""
        def __init__(self):
                self.serial=functions.mySerial()
                with app.frame("controlPage"): 
                        with app.frame("milliLeftButtons",0,0,1,1):
                                app.addIconButton("milliExitButton",lambda: app.stop(), "exit",0,0)
                                app.setButtonBg("milliExitButton","red")
                                functions.spacer(0,1,1,1)
                                app.addImage("milliSpinner","Directory/Images/loading.gif",1,0)
                                app.setAnimationSpeed("milliSpinner",60)
                                app.hideImage("milliSpinner")

                        app.addLabel("milliMenuTitle","millIGAT Pump Control",0,2,1,1)

                        with app.frame("milliRightButtions",0,4,1,1):
                                app.addIconButton("milliHomeButton",lambda: functions.homeScreen(),"arrow-1-left",0,0) 
                                app.addIconButton("milliSerialRefresh",self.serial.testConnection,"connect-alt-1",1,0)
                                app.setButtonBg("milliHomeButton","lightGrey")
                                app.setButtonBg("milliSerialRefresh","lightGrey")

                        functions.spacer(0,1,1,1)
                        functions.spacer(0,3,1,1)

                
                with app.tabbedFrame("milliGUI"): 
                        with app.tab("Home"):
                                app.setBg("white")
                                with app.frame("milliLeft",0,0):
                                        with app.frame("milliAspirate"):
                                                app.addLabel("AspirateTitle","Aspirate")
                                                with app.frame("milliAspirateButtons"):
                                                        app.addIconButton("leftAspirate",lambda: self.aspirate("left"),"arrow-1-left",0,0)
                                                        app.addIconButton("stopAspirate",lambda: self.aspirate("stop"),"stop-alt",0,1)
                                                        app.addIconButton("rightAspirate",lambda: self.aspirate("right"),"arrow-1-right",0,2)
                                                        app.setButtonBg("leftAspirate","lightGreen")
                                                        app.setButtonBg("stopAspirate","red")
                                                        app.setButtonBg("rightAspirate","lightGreen")

                                        with app.frame("milliImage"):
                                                app.addImage("milliGATImage","Directory/Images/milliGAT.png",0,0)
                                                app.addIcon("leftFlow","arrow-1-left",1,0)
                                                app.addIcon("rightFlow","arrow-1-right",1,0)
                                                app.addIcon("stopFlow","stop-alt",1,0)
                                                app.hideImage("leftFlow")
                                                app.hideImage("rightFlow")
                                                app.setImageBg("leftFlow","lightGreen")
                                                app.setImageBg("rightFlow","lightGreen")

                                        with app.frame("milliSlew"):
                                                app.addLabel("SlewTitle","Slew")
                                                with app.frame("milliSlewButtons"):
                                                        app.addIconButton("leftSlew",lambda: self.slew("left"),"arrow-1-backward",0,0)
                                                        app.addIconButton("stopSlew",lambda: self.slew("stop"),"stop-alt",0,1)
                                                        app.addIconButton("rightSlew",lambda: self.slew("right"),"arrow-1-forward",0,2)
                                                        app.setButtonBg("leftSlew","lightGreen")
                                                        app.setButtonBg("stopSlew","red")
                                                        app.setButtonBg("rightSlew","lightGreen")

                                with app.frame("milliRight",0,1):
                                        app.setPadding([10,10])
                                        app.addLabel("milliAddressText","Pump Address: ",0,0)
                                        app.addOptionBox("milliAddress",["-select Address-",]+variables.connectedmilliGAT,0,1,2)
                                        app.setOptionBoxBg("milliAddress","lightGrey")
                                        app.addLabel("milliVolumeText1","Volume: ",1,0)
                                        app.addNamedButton(str(self.milliVar.volume),"milliVolume",lambda btn: numPadInit.pad.show(5,0,btn,self),1,1)
                                        app.setButtonBg("milliVolume","lightGrey")
                                        app.getButtonWidget("milliVolume").config(font=20)
                                        app.addLabel("milliVolumeText2","µl",1,2)
                                        app.setLabelSticky("milliVolumeText2","nws")

               
                                        app.addLabel("milliFlowRateText","FlowRate: ",2,0)
                                        app.addNamedButton(str(self.milliVar.flowRate),"milliFlowRate",lambda btn: numPadInit.pad.show(5,0,btn,self) ,2,1)
                                        app.setButtonBg("milliFlowRate","lightGrey")
                                        app.getButtonWidget("milliFlowRate").config(font=20)
                                        app.addLabel("milliFlowRateText2","µl/sec",2,2)
                                        app.setLabelSticky("milliFlowRateText2","nws")
                                        with app.frame("milliFillFrame",3,0,3):
                                                app.addMeter("milliFill")
                                                app.setMeterFill("milliFill","green")

                        with app.tab("Settings"):
                                app.setBg("white")
                                app.addIconButton("milExitButton",lambda: app.stop(), "exit",)




        def aspirate(self, direction):
                address=app.getOptionBox("milliAddress")
                if str(address)!="None":
                        app.setImageBg("milliGATImage","lightGreen")
                        items=["rightAspirate","leftAspirate","rightSlew","leftSlew","stopSlew"]
                        if direction=="left":
                                app.hideImage("stopFlow")
                                app.showImage("leftFlow")
                                for i in items:
                                        app.disableButton(i)
                                self.serial.write((str(address)+"VM "+str(self.milliVar.flowRate*809)+"\n").encode())
                                self.serial.write((str(address)+"VL -"+str(self.milliVar.volume)+"\n").encode())
                                self.serial.write((str(address)+"EX FL\n").encode())                             
                        elif direction=="right":
                                app.hideImage("stopFlow")
                                app.showImage("rightFlow")
                                self.serial.write((str(address)+"VM "+str(self.milliVar.flowRate*809)+"\n").encode())
                                self.serial.write((str(address)+"VL "+str(self.milliVar.volume)+"\n").encode())
                                self.serial.write((str(address)+"EX FL\n").encode())
                                for i in items:
                                        app.disableButton(i)
                        elif direction=="stop":
                                app.hideImage("rightFlow")
                                app.hideImage("leftFlow")
                                app.showImage("stopFlow")
                                for i in items:
                                        app.enableButton(i)
                                app.setImageBg("milliGATImage","white")

                                self.serial.write((str(address)+"SL 0\n").encode())


                        """startTime=time.time()
                        runTime=self.milliVar.volume/self.milliVar.flowRate
                        def updateMilliMeter():
                                getTime=time.time()
                                app.setMeter("progress", ((getTime-startTime)/runTime)*100)
                        app.registerEvent(updateMilliMeter)"""

                else:
                        app.errorBox("Pump Not Selected","Please select pump address", parent=None)


        def slew(self,direction):
                self.serial=functions.mySerial()
                address=app.getOptionBox("milliAddress")

                if str(address)!= "None":
                        print(app.getImageBg("milliGATImage"))
                        app.setImageBg("milliGATImage","lightGreen")
                        items=["rightAspirate","leftAspirate","rightSlew","leftSlew","stopAspirate"]
                        if direction=="left":
                                app.hideImage("stopFlow")
                                app.showImage("leftFlow")
                                for i in items:
                                        app.disableButton(i)
                                self.serial.write((str(address)+"SL -"+str(self.milliVar.flowRate*809)+"\n").encode())
                        elif direction=="right":
                                app.hideImage("stopFlow")
                                app.showImage("rightFlow")
                                for i in items:
                                        app.disableButton(i)
                                self.serial.write((str(address)+"SL "+str(self.milliVar.flowRate*809)+"\n").encode())
                        elif direction=="stop":
                                app.hideImage("rightFlow")
                                app.hideImage("leftFlow")
                                app.showImage("stopFlow")
                                for i in items:
                                        app.enableButton(i)
                                app.setImageBg("milliGATImage","white")

                                self.serial.write((str(address)+"SL 0\n").encode())

                else:
                        app.errorBox("Pump Not Selected","Please select pump address", parent=None)

                        







