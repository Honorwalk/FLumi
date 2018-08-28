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
        eu=0
        set2=0
        def __init__(self):
                self.serial=functions.mySerial()
                self.address=variables.address(serial)
                
                with app.frame("controlPage"): 
                        with app.frame("milliLeftButtons",0,0,1,1):
                                app.setPadding([5,5])
                                app.addIconButton("milliExitButton",lambda: app.stop(), "exit",0,0)
                                app.setButtonBg("milliExitButton","red")
                                app.addIconButton("milliHomeButton",lambda: functions.homeScreen(),"arrow-1-left",0,1)
                                app.setButtonBg("milliHomeButton","lightGrey") 

                        app.addLabel("milliMenuTitle","millIGAT Pump Control",0,2,1,1)

                        with app.frame("milliRightButtions",0,4,1,1):
                                app.setPadding([5,5])
                                app.addIconButton("milliSerialRefresh",lambda: self.serial.testConnection(self,1),"connect-alt-1",0,1)
                                app.addOptionBox("milliAddress",["-select Address-",]+self.address.milliGAT,0,0)
                                app.setOptionBoxChangeFunction("milliAddress",self.getSettings)
                                app.addImage("milliSpinner","Directory/Images/loading.gif",0,1)
                                app.setAnimationSpeed("milliSpinner",60)
                                app.hideImage("milliSpinner")
                                app.setButtonBg("milliSerialRefresh","lightGrey")
                                app.setImageBg("milliSpinner","lightGrey")
                                

                        functions.spacer(0,1,1,1)
                        functions.spacer(0,3,1,1)

                
                with app.tabbedFrame("milliGUI"): 
                        with app.tab("Home"):
                                app.setPadding([10,10])
                                app.setBg("white")
                                with app.frame("milliLeft",0,0):
                                        with app.frame("milliAspirate"):
                                                app.addLabel("AspirateTitle","Pump")
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
                                app.setPadding([10,10])
                                app.setBg("white")
                                with app.frame("settingsLeft",1,0):
                                        with app.frame("eu"):
                                                app.addLabel("euLabel","EU: ",0,0)
                                                app.addLabel("euText",str(self.milliVar.eu),0,1)
                                        with app.frame("set2"):
                                                app.addLabel("set2Label","s2: ",0,0)
                                                app.addLabel("set2Text","??",0,1)
                                        with app.frame("set3"):
                                                app.addLabel("set3Label","s3: ",0,0)
                                                app.addLabel("set3Text","??",0,1)
                                with app.frame("settingsRight",1,1):
                                        with app.frame("set4"):
                                                app.addLabel("set4Label","s4: ",0,0)
                                                app.addLabel("set4Text","??",0,1)
                                        with app.frame("set5"):
                                                app.addLabel("set5Label","s5: ",0,0)
                                                app.addLabel("set5Text","??",0,1)
                                        with app.frame("set6"):
                                                app.addLabel("set6Label","s6: ",0,0)
                                                app.addLabel("set6Text","??",0,1)
                                        
                                        

        def aspirate(self, direction):
                self.percent=0
                address=app.getOptionBox("milliAddress")
                if str(address)!="None":
                        self.serial.connect()
                        if self.serial.connected==1:
                                app.setImageBg("milliGATImage","lightGreen")
                                items=["rightAspirate","leftAspirate","rightSlew","leftSlew","stopSlew"]
                                if direction=="left":
                                        app.hideImage("stopFlow")
                                        app.showImage("leftFlow")
                                        for i in items:
                                                app.disableButton(i)
                                        self.serial.write((str(address)+"VM "+str(self.milliVar.flowRate*self.eu)+"\n"))
                                        self.serial.write((str(address)+"VL -"+str(self.milliVar.volume)+"\n"))
                                        self.serial.write((str(address)+"EX FL\n"))    
                                        self.startTime=time.time()
                                        self.percent=0
                                        app.registerEvent(self.updateMeter) 
                                        app.setPollTime(10)                
                        
                                elif direction=="right":
                                        app.hideImage("stopFlow")
                                        app.showImage("rightFlow")
                                        for i in items:
                                                app.disableButton(i)
                                        self.serial.write((str(address)+"VM "+str(self.milliVar.flowRate*self.eu)+"\n"))
                                        self.serial.write((str(address)+"VL "+str(self.milliVar.volume)+"\n"))
                                        self.serial.write((str(address)+"EX FL\n"))
                                        self.startTime=time.time() 
                                        self.percent=0 
                                        app.registerEvent(self.updateMeter)  
                                        app.setPollTime(10)                
                                        
                                elif direction=="stop":
                                        app.hideImage("rightFlow")
                                        app.hideImage("leftFlow")
                                        app.showImage("stopFlow")
                                        for i in items:
                                                app.enableButton(i)
                                        app.setImageBg("milliGATImage","white")

                                        self.serial.write((str(address)+"SL 0\n"))
                                        self.percent=0
                                        app.setMeter("milliFill",self.percent)
                                        self.percent=200
                                self.serial.disconnect()
                else:
                        app.errorBox("Pump Not Selected","Please select pump address", parent=None)

        def slew(self,direction):
                address=app.getOptionBox("milliAddress")
                if str(address)!= "None":
                        self.serial.connect()
                        if self.serial.connected==1:
                                app.setImageBg("milliGATImage","lightGreen")
                                items=["rightAspirate","leftAspirate","rightSlew","leftSlew","stopAspirate"]
                                if direction=="left":
                                        app.hideImage("stopFlow")
                                        app.showImage("leftFlow")
                                        for i in items:
                                                app.disableButton(i)
                                        self.serial.write((str(address)+"SL -"+str(self.milliVar.flowRate*809)+"\n"))
                                elif direction=="right":
                                        app.hideImage("stopFlow")
                                        app.showImage("rightFlow")
                                        for i in items:
                                                app.disableButton(i)
                                        self.serial.write((str(address)+"SL "+str(self.milliVar.flowRate*809)+"\n"))
                                elif direction=="stop":
                                        app.hideImage("rightFlow")
                                        app.hideImage("leftFlow")
                                        app.showImage("stopFlow")
                                        for i in items:
                                                app.enableButton(i)
                                        app.setImageBg("milliGATImage","white")
                                        self.serial.write((str(address)+"SL 0\n"))
                                self.serial.disconnect()

                else:
                        app.errorBox("Pump Not Selected","Please select pump address or connect devices", parent=None)

        def updateMeter(self):
                if self.percent<100: 
                        sinceStart=time.time()-self.startTime
                        self.percent=(sinceStart/(self.milliVar.volume/self.milliVar.flowRate))*100
                        app.setMeter("milliFill",self.percent)
                elif 100<self.percent<105: 
                        self.aspirate("stop")
   
        def getSettings(self):
                selAddress=app.getOptionBox("milliAddress")
                index=self.address.milliGAT.index(selAddress)
                settings=self.address.milliGATSettings[index]
                self.eu=settings[0]
                self.set2=settings[1]
                app.setLabel("euText",str(self.eu))
                app.setLabel("set2Text",str(self.set2))

