milliGATAdd="A"
valcoAdd="A"
OMRONAdd="A"

from appJar import *
import functions

def loadHome(boot):
    app = gui("Flumi", "800x480")
    app.setBg("lightGrey")
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(size=10)
    app.setLabelFont(size=20)
    if boot=="boot":
        app.showSplash("Fluidics Machine Interface", fill="darkGrey", stripe="white", fg="black", font="50")

    
    for x in range(25):
        app.addLabel("side%s"%(x),"",0,x)
    for y in range(1,15):
        app.addLabel("top%s"%(y),"",y,0)
        
    app.addImage("logo","images/logo220.png",0,0,25,5)
    app.zoomImage("logo",2)

    app.addIconButton("milliGATButton",functions.press,"arrow-1-up",6,3,4,2)
    app.addLabel("milliGATLabel","milliGAT Pump",6,8,6,1)
    app.addLabel("milliGATAddressText","Address: ",7,10,5,1)
    app.addNamedButton(milliGATAdd,"milliGATAddress",functions.press,7,14,1,1)
    app.setButtonBg("milliGATButton","darkGreen")
    
    app.addIconButton("valcoButton",functions.press,"arrow-1-up",9,3,4,2)
    app.addLabel("valcoLabel","Valco Valve",9,8,6,1)
    app.addLabel("valcoAddressText","Address: ",10,10,5,1)
    app.addNamedButton(valcoAdd,"valcoAddress",functions.press,10,14,1,1)
    app.setButtonBg("valcoButton","darkGreen")



    app.addIconButton("OMRONButton",functions.press,"arrow-1-up",12,3,4,2)
    app.addLabel("OMRONLabel","OMRON Temp",12,8,6,1)
    app.addLabel("OMRONAddressText","Address: ",13,10,5,1)
    app.addNamedButton(OMRONAdd,"OMRONAddress",functions.press,13,14,1,1)
    app.setButtonBg("OMRONButton","darkGreen")
 
    app.getLabelWidget("valcoAddressText").config(font=15)
    app.getLabelWidget("milliGATAddressText").config(font=15)
    app.getLabelWidget("OMRONAddressText").config(font=15)
    
    app.go()
