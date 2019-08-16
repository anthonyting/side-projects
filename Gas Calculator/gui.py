import tkinter as tk
import calculate as c
import re
from units import *

def evaluate(string):
    string = re.sub("^0+","",string)
    return eval(string) if string else 0

def focusNext(event):
    event.widget.tk_focusNext().focus()

class GasButtons:
    
    def __init__(self, master):
        # initializes the gui
        self.f = tk.Frame(master)
        self.f.pack(padx=10, pady=10)

        self.rateUnit = rateUnit()
        self.distanceUnit = distanceUnit()
        self.priceUnit = priceUnit()

        self.initLabels()
        self.initEntries()

        self.f.grid_columnconfigure(0,minsize=190)

        # creating the submit button
        self.submitButton = tk.Button(self.f, text = "Check", command = lambda: self.result(self.f), font=("Segoe UI", 15))
        self.submitButton.grid(row=3,columnspan=3)
        self.submitButton.bind("<Return>", lambda event: self.result(self.f))

        self.initToggle()

    def initLabels(self):
        # creating the entry labels
        self.rateLabelVar = tk.StringVar()
        self.rateLabelVar.set(f"Fuel Economy ({self.rateUnit.type})")

        self.distanceLabelVar = tk.StringVar()
        self.distanceLabelVar.set(f"Distance ({self.distanceUnit.type})")

        self.priceLabelVar = tk.StringVar()
        self.priceLabelVar.set(f"Gas Price (¢/{self.priceUnit.type})")

        self.rateLabel = tk.Label(self.f, textvariable=self.rateLabelVar, font=("Segoe UI", 15))
        self.distanceLabel = tk.Label(self.f, textvariable=self.distanceLabelVar, font=("Segoe UI", 15))
        self.priceLabel = tk.Label(self.f, textvariable=self.priceLabelVar, font=("Segoe UI", 15))

        self.rateLabel.grid(row=0, sticky=tk.E)
        self.distanceLabel.grid(row=1, sticky=tk.E)
        self.priceLabel.grid(row=2, sticky=tk.E)

    def initEntries(self):
        # creating the three entry boxes
        self.rateEntry = tk.Entry(self.f, font=("Segoe UI", 15))
        self.distanceEntry = tk.Entry(self.f, font=("Segoe UI", 15))
        self.priceEntry = tk.Entry(self.f, font=("Segoe UI", 15))

        self.rateEntry.grid(row=0, column=1)
        self.distanceEntry.grid(row=1, column=1)
        self.priceEntry.grid(row=2, column=1)

        # enter/down/up key on every entry
        self.rateEntry.bind("<Down>", focusNext)
        self.rateEntry.bind("<Return>", focusNext)
        self.distanceEntry.bind("<Return>", focusNext)
        self.distanceEntry.bind("<Down>", focusNext)
        self.distanceEntry.bind("<Up>", lambda e: self.rateEntry.focus_set())
        self.priceEntry.bind("<Up>", lambda e: self.distanceEntry.focus_set())

        # enter key on the last entry
        self.priceEntry.bind("<Return>", lambda e: self.result(self.f))
    
    def initToggle(self):
        # creating the toggle
        
        def rateToggle():
            self.rateUnit.switch()
            self.rateLabelVar.set(f"Fuel Economy ({self.rateUnit.type})")
        
        def distanceToggle():
            self.distanceUnit.switch()
            self.distanceLabelVar.set(f"Distance ({self.distanceUnit.type})")

        def priceToggle():
            self.priceUnit.switch()
            self.priceLabelVar.set(f"Gas Price (¢/{self.priceUnit.type})")

        rateButton = tk.Button(self.f, text="Change Unit", command=rateToggle, font=("Segoe UI", 15))
        distanceButton = tk.Button(self.f, text="Change Unit", command=distanceToggle, font=("Segoe UI", 15))
        priceButton = tk.Button(self.f, text="Change Unit", command=priceToggle, font=("Segoe UI", 15))

        rateButton.grid(row=0,column=2,sticky=tk.W)

        distanceButton.grid(row=1,column=2,sticky=tk.W)
        priceButton.grid(row=2,column=2,sticky=tk.W)

    def showRes(self,string):
        # show result
        try:
            # will set every time but first time
            self.text_var.set(string)
        except:
            # init result label
            self.text_var = tk.StringVar(self.f)
            resultLabel = tk.Label(self.f, textvariable=self.text_var, font=("Segoe UI", 15))
            self.text_var.set(string)
            resultLabel.grid(row=4,columnspan=3)

    def result(self,master):
        try:
            # calculate
            rate = evaluate(self.rateEntry.get())
            distance = evaluate(self.distanceEntry.get())
            price = evaluate(self.priceEntry.get())

            rate = c.rate(rate,self.rateUnit.type)
            distance = c.distance(distance,self.distanceUnit.type)
            price = c.price(price,self.priceUnit.type)

            calculated = c.calculate(rate,distance,price)

            self.showRes(f"Total Cost: ${calculated:.2f}")

        except ZeroDivisionError:
            print ("Error: Dividing by Zero")
            self.showRes("Error: Dividing by Zero")

root = tk.Tk()
root.resizable(0,0)
root.title("Gas Calculator")
g = GasButtons(root)
root.mainloop()