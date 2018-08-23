from appJar import gui
from . import functions
from . import variables
app=variables.variables.get(1)
milliGATAdd=variables.variables.get(2)
valcoAdd=variables.variables.get(3)
OMRONAdd=variables.variables.get(4)
def loadValcoHome():
        app.addIconButton("valcoExitButton",lambda: app.stop(), "exit",0,0,1,1)
        app.setButtonBg("valcoExitButton","red")
        app.addLabel("valcoMenuTitle","Valco Valve Control",0,1,1,1)
        app.addIconButton("valcoHomeButton",lambda: functions.homeScreen(),"arrow-1-left",0,2,1,1)             
       




