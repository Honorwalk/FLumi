from appJar import gui
from Directory import Homescreen
from Directory import milliGAT
from Directory import valco
from Directory import OMRON
from Directory import functions
from Directory import numPad
from Directory.variables import variables
from Directory import numPadInit


app=variables.get(1)
app.setBg("lightGrey")
app.setSticky("news")
app.setExpand("both")
app.setFont(size=10)
app.setLabelFont(size=20)
app.setPadding([20,0])

#app.showSplash("Fluidics Machine Interface", fill="darkGrey", stripe="white", fg="black", font="50")
with app.frameStack("Pages", start=0):
    with app.frame():
        Homescreen.loadHome()
    with app.frame():
        milliGAT.milliGATHome()
    with app.frame():
        valco.loadValcoHome()
    with app.frame():
        OMRON.loadOMRONHome()

app.go()
if app.exitFullscreen():
    app.stop()



    



 






