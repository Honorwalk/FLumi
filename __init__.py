from appJar import gui
from Directory import Homescreen
from Directory import milliGAT
from Directory import valco
from Directory import OMRON
from Directory import functions
from Directory import variables



app=variables.variables.get(1)
app.setBg("Grey")
app.setSticky("news")
app.setExpand("both")
app.setFont(size=10)
app.setLabelFont(size=20)
app.setOnTop(stay=True)

app.showSplash("Fluidics Machine Interface", fill="darkGrey", stripe="white", fg="black", font="50")

with app.frameStack("Pages", start=0):
    with app.frame("home",0,0,25,16):
        Homescreen.loadHome()
    with app.frame("milliGAT",0,0,25,16):
        milliGAT.loadMilliGATHome()
    with app.frame("Valco",0,0,25,16):
        valco.loadValcoHome()
    with app.frame("OMRON",0,0,25,16):
        OMRON.loadOMRONHome()
app.setPadding([0,0])

if app.exitFullscreen():
    app.stop()
app.go()




    



 






