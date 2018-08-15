from appJar import gui
import milliGAT


def press(btn):
        print(btn)

def layout(run,app):
        for x in range(25):
                app.addLabel(str(run)+"side%s"%(x),"",0,x)
        for y in range(1,15):
                app.addLabel(str(run)+"top%s"%(y),"",y,0)
def switchPage(btn, variables):
        app=variables.get(1)
        app.selectFrame("Pages",1,callFunction=True)
        app.selectFrame("Control",btn,callFunction=True)
def loadMenu(variables):
        app=variables.get(1)
        app.addIconButton("HomeButton",lambda: app.selectFrame("Pages",0,callFunction=True),"arrow-1-up",6,3,4,2)

               
        





    
