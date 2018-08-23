from appJar import gui
from . import variables
app=variables.variables.get(1)

class newPad():
    entry=""
    obj=""
    def show(self,length,deci,btn,obj):
        
        self.entry=""
        self.length=length
        self.disabled=0
        self.deci=deci
        self.btn=btn
        self.obj=obj
        app.showSubWindow("numPad")
        if self.deci==0:
            app.disableButton("button.")
        else:
            app.enableButton("button.")
        app.getLabelWidget("Entry").config(text=self.entry)
        self.compatCheck()
    
    def __init__(self):
        self.numbers=[[7,8,9],[4,5,6],[1,2,3]]
        with app.subWindow("numPad",title="numPad",modal=True):
            app.setExpand("both")
            app.setSticky("news")
            app.setSize(400,400)
            app.setPadding([10,10])
            with app.frame("entryFrame"):
                app.setSticky("nws")
                app.setBg("darkGrey")
                app.label("Entry",str(self.entry))

            with app.frame("pad"):
                app.addNamedButton("1","button1",lambda: self.enter("1"),2,0)
                app.addNamedButton("2","button2",lambda: self.enter("2"),2,1)
                app.addNamedButton("3","button3",lambda: self.enter("3"),2,2)
                app.addNamedButton("4","button4",lambda: self.enter("4"),1,0)
                app.addNamedButton("5","button5",lambda: self.enter("5"),1,1)
                app.addNamedButton("6","button6",lambda: self.enter("6"),1,2)
                app.addNamedButton("7","button7",lambda: self.enter("7"),0,0)
                app.addNamedButton("8","button8",lambda: self.enter("8"),0,1)
                app.addNamedButton("9","button9",lambda: self.enter("9"),0,2)
                app.addNamedButton("0","button0",lambda: self.enter("0"),3,1)
                app.addNamedButton(".","button.",lambda: self.enter("."),4,1)
                app.addIconButton("undo",lambda: self.back(),"arrow-1-left",3,0,1,2)
                app.addButton("Go",lambda: self.go(),3,2,1,2)

            for i in range(0,10):
                app.getButtonWidget("button"+str(i)).config(font="20")
            app.getButtonWidget("button.").config(font="20")
            app.setButtonBg("undo","red")
            app.setButtonBg("Go","green")
   
    def enter(self,number):
        self.entry+=number
        app.getLabelWidget("Entry").config(text=self.entry)
        if number==".":
            app.disableButton("button.")
        self.compatCheck()

    def back(self):
        if self.entry[-1:]==".":
                    app.enableButton("button.")
        self.entry=self.entry[0:-1]
        app.getLabelWidget("Entry").config(text=self.entry)
        self.compatCheck()

    def go(self):
    #volume
        if self.btn=="milliVolume":
            self.obj.milliVar.volume=float(self.entry)
            print(self.obj.milliVar.volume) 
    #flow Rate
        elif self.btn=="milliFlowRate":
            self.obj.milliVar.flowRate=float(self.entry)
            print(self.obj.milliVar.flowRate) 
        self.obj.milliVar.save()
        app.setButton(self.btn,float(self.entry))
        app.hideSubWindow("numPad")  




    def compatCheck(self):
        if len(self.entry.replace(".",""))==self.length and self.disabled==0:
            for i in range(10):
                app.disableButton("button"+str(i))
            self.disabled=1
        elif len(self.entry.replace(".",""))<self.length and self.disabled==1:
            for i in range(10):
                app.enableButton("button"+str(i))
            self.disabled=0


