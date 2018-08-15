from appJar import gui
import Homescreen
import milliGAT
import valco
import OMRON
import functions



variables={
    1 : gui("Flumi", "800x480"),
    2 : "A",
    3 : "A",
    4 : "A"
    }
app=variables.get(1)
app.setBg("lightGrey")
app.setSticky("news")
app.setExpand("both")
app.setFont(size=10)
app.setLabelFont(size=20)
app.showSplash("Fluidics Machine Interface", fill="darkGrey", stripe="white", fg="black", font="50")

        
with app.frameStack("Pages", start=0):
    with app.frame("home"):
        Homescreen.loadHome(variables)
    with app.frame("controlDeck"):
        with app.frameStack("Control"):
            functions.layout(1,app)
            functions.loadMenu(variables)
            with app.frame("milliGAT"):
                milliGAT.loadMilliGATHome(variables)
            with app.frame("Valco"):
                valco.loadValcoHome(variables)
            with app.frame("OMRON"):
                OMRON.loadOMRONHome(variables)
app.go()


    



 






