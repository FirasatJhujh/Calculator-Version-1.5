from tkinter import *

root = Tk()

class Calculator():
    def __init__(self,master):
        self.root = master
        # Set width and height
        self.root.geometry("1200x700")
        # Set maxsize
        self.root.maxsize(595,495)
        # Set calculator
        self.root.title("Caculator")
        self.root.wm_iconbitmap("calculator-icon.ico")
        self.Ans = '0'
        self.scvalue = StringVar()
        # validation = root.register()

        self.screen = Entry(self.root,textvariable=self.scvalue,font="comic 25",borderwidth=30,relief="sunken",state="readonly").pack(anchor="nw",ipadx=80,padx=4)
        self.buttonsFrame = Frame(self.root)
        
        self.b1 = Button(self.buttonFrameRow1,text="1",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=42,ipady=10,padx=2,pady=5)
    
        self.b1 = Button(self.buttonFrameRow1,text="2",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="3",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="DEL",font="comic 25",background="pink")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=8,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="AC",font="comic 25",background="pink")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=13,ipady=10,padx=2,pady=5)
        
        self.buttonFrameRow1.pack(anchor="nw",padx=3)

        self.buttonFrameRow1 = Frame(self.buttonsFrame)
        self.b1 = Button(self.buttonFrameRow1,text="4",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=43,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="5",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="6",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=31,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="x",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="/",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.buttonFrameRow1.pack(anchor="nw",padx=3)

        self.buttonFrameRow1 = Frame(self.buttonsFrame)
        
        self.b1 = Button(self.buttonFrameRow1,text="7",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=43,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="8",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="9",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=31,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="+",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="-",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=31,ipady=10,padx=2,pady=5)

        self.buttonFrameRow1.pack(anchor="nw",padx=3)

        self.buttonFrameRow1 = Frame(self.buttonsFrame)
        self.b1 = Button(self.buttonFrameRow1,text="0",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=43,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text=".",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=33,ipady=10,padx=2,pady=5)


        self.b1 = Button(self.buttonFrameRow1,text="%",font="comic 25",)
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=31,ipady=10,padx=2,pady=5)


        self.b1 = Button(self.buttonFrameRow1,text="Ans",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=13,ipady=10,padx=2,pady=5)

        self.b1 = Button(self.buttonFrameRow1,text="=",font="comic 25")
        self.b1.bind("<Button-1>",self.calculate)
        self.b1.pack(side="left",anchor="nw",ipadx=28,ipady=10,padx=2,pady=5)


        self.buttonFrameRow1.pack(anchor="nw",padx=3)

        self.buttonsFrame.pack(anchor="nw")
    def calculate(self,event):
        self.text = event.widget.cget("text")
        self.value = self.scvalue.get()
        if (self.text == "="):
            self.value = self.value.replace("x","*")
            if "Ans" in self.value:
                self.prevalue = self.value.replace("Ans",str(self.Ans))
                self.Ans = eval(self.prevalue) # 35 
                print("\n"+str(self.Ans))
                self.Ans = str(self.Ans)
                self.value = self.Ans.replace("Ans",str(self.Ans))
                self.result = eval(self.value)
                print(self.prevalue)
                print(self.value)
                print(self.result)
                self.scvalue.set(self.result)
            else:
                self.Ans = eval(self.value)
                self.result = eval(self.value)
                self.scvalue.set(self.result)
                print(str(self.Ans))

        elif(self.text == "DEL"):
            self.scvalue.set(self.scvalue.get()[0:-1])

        elif (self.text == "AC"):
            self.scvalue.set("")
        else:
            self.scvalue.set(self.scvalue.get() + self.text)

A = Calculator(root)

root.mainloop()