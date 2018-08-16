from appJar import gui
import Homescreen
import milliGAT
import valco
import OMRON
import functions
import variables



app=variables.variables.get(1)
app.setBg("Grey")
app.setSticky("news")
app.setExpand("both")
app.setFont(size=10)
app.setLabelFont(size=20)
app.setOnTop(stay=True)

#app.showSplash("Fluidics Machine Interface", fill="darkGrey", stripe="white", fg="black", font="50")
with app.frameStack("Pages", start=0):
    with app.frame("home"):
        functions.layout()
        Homescreen.loadHome()
    with app.frame("controlDeck"):
        with app.frameStack("Control"):
            functions.layout()
            functions.loadMenu()
            with app.frame("milliGAT"):
                milliGAT.loadMilliGATHome()
            with app.frame("Valco"):
                valco.loadValcoHome()
            with app.frame("OMRON"):
                OMRON.loadOMRONHome()
app.go()



    



 






