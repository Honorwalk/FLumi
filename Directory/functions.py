from appJar import gui
def press(btn):
        print(btn)


def layout(run,app):
        for x in range(25):
                app.addLabel(str(run)+"side%s"%(x),"",0,x)
        for y in range(1,15):
                app.addLabel(str(run)+"top%s"%(y),"",y,0)






    
