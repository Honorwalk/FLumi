from appJar import gui
import serial
try: 
    import cPickle as pickle
except ImportError:
    import pickle
variables={
    1 : gui("Flumi", "fullscreen"),
    #1 : gui("Flumi", "800x480"),
    2 : "A",
    3 : "A",
    4 : "A"
    }
layouts=0
menus=0
spacers=0
connectedmilliGAT=[]
connectedValco=[]
connectedOMRON=[]



class milliGAT():
    def __init__(self):
        loadedClass=self.load()
        if hasattr(loadedClass,'address')==0:
            self.volume=0
            self.flowRate=0
            self.eu=0
            self.address=[]
        else:
            self.volume=loadedClass.volume
            self.flowRate=loadedClass.flowRate
            self.eu=loadedClass.eu
            self.address=loadedClass.address
        self.save()
    def save(self):
        pickleOut=open("variables/milliGAT.pickle","wb")
        pickle.dump(self,pickleOut)
        pickleOut.close()
    def load(self):
        pickleIn=open("variables/milliGAT.pickle","rb")
        self=pickle.load(pickleIn)
        return self


