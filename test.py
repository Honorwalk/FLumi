from appJar import gui
from Directory import Homescreen
from Directory import milliGAT
milliGATAdd="A"
valcoAdd="A"
OMRONAdd="A"

with gui("Flumi", "800x480") as app:
    app.setBg("lightGrey")
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(size=10)
    app.setLabelFont(size=20)
    app.showSplash("Fluidics Machine Interface", fill="darkGrey", stripe="white", fg="black", font="50")

        
    with app.frameStack("Pages", start=0):
        with app.frame("home"):
            Homescreen.loadHome(app,milliGATAdd,valcoAdd,OMRONAdd)
        with app.frame("milliGAT"):
            milliGAT.loadMilliGATHome(app,milliGATAdd,valcoAdd,OMRONAdd)


 






