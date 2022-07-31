from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import *
import sys


class Builder():

    # retrieve values from entry fiends, run calculations, and place them in window 2
    def get_tax_bill(self):
    #open window 2 and set minimum size
        print("Printing your final bill")
        window2 = tk.Tk()
        window2.minsize(420, 220)
        window2.maxsize(450, 250)
        window2.title("Property Tax Bill")

        # This is the label for Assessed Value in Window 2
        self.bLabel = Label(window2, text='Real Property Value', fg='green', font=("Courier", 14, "underline"))
        self.bLabel.pack()

        # This is the label for Assessed Value in Window 2
        self.cLabel = Label(window2, text='Assessed Value', fg='green', font=("Courier", 14))
        self.cLabel.pack()

        # This is the label for Monthly Taxes in window 2
        self.dLabel = Label(window2, text='Monthly Tax Bill', fg='blue')
        self.dLabel.pack()

        # This is the label for Monthly HOA fees in window 2
        self.eLabel = Label(window2, text='Monthly HOA Fees', fg='blue')
        self.eLabel.pack()

        # This is the label for total tax bill in window 2
        self.fLabel = Label(window2, text='Total Monthly Bill', fg='red', font=("Courier", 14))
        self.fLabel.pack()

        # This is the label for Annual Tax Bill in window 2
        self.gLabel = Label(window2, text='Annual Tax Bill', fg='blue')
        self.gLabel.pack()

        # This is the label for Annual HOA Fees in window 2
        self.hLabel = Label(window2, text='Annual HOA Fees', fg='blue')
        self.hLabel.pack()

        #This is the label for Total Annual Expensesin window 2
        self.iLabel = Label(window2, text='Total Annual Expenses', fg='red', font=("Courier", 20, "underline"))
        self.iLabel.pack()


        self.bLabel.configure(text="Real Property Value: $"+str("{:,.2f}".format(self.real_prop_value)))
        self.cLabel.configure(text="Assessed Property Value: $"+str("{:,.2f}".format(self.avCalc)))
        self.dLabel.configure(text="Monthly Tax Bill: $"+str("{:,.2f}".format(self.assessed_monthly_tax)))
        self.eLabel.configure(text="Monthly HOA Fees: $"+str("{:,.2f}".format(self.monthly_hoa)))
        self.fLabel.configure(text="Total Monthly Bill: $"+str("{:,.2f}".format(self.total_monthly_bill)))
        self.gLabel.configure(text="Annual Tax Bill: $"+str("{:,.2f}".format(self.assessed_yearly_tax)))
        self.hLabel.configure(text="Annual HOA Fees: $"+str("{:,.2f}".format(self.yearly_hoa)))
        self.iLabel.configure(text="Total Annual Bill: $"+str("{:,`.2f}".format(self.total_yearly_bill)))

    def calculate(self):
        print("enter calc function")
        # gets the two entry fields, converts each to floats then runs calc on them
        #get Real Property Value from Entry widget and convert to workable variable
        rpv = float(self.rpvEntry.get())
        self.real_prop_value = rpv
        #Calculate Assessed Property Value at 60% of rpv
        self.avCalc = rpv * .6
        #calculate Monthly Tax Bill by multiplying Assessed Prop Value * .0075 ($.75 for every $100)
        self.assessed_monthly_tax = self.avCalc * .0075
        #calc yearly Tax by multiplying by 12
        self.assessed_yearly_tax = self.assessed_monthly_tax *12

        # get the HOA fee from second entry field and convert to workable variable
        hoa = float(self.hoaEntry.get())
        self.monthly_hoa = hoa
        #Calc yearly HOA by multilplying monthly by 12
        self.yearly_hoa = hoa * 12

        #calculate total monthly and yearly bills
        self.total_monthly_bill = self.assessed_monthly_tax + self.monthly_hoa
        self.total_yearly_bill = self.assessed_yearly_tax + self.yearly_hoa
        self.get_tax_bill()

    #validate that all values in the both entry strings are digits
    def validate(self):
        #convert variables to strings and rename for local scope
        print("inside VALIDATE")
        validrpv = str(self.rpvEntry.get())
        validhoa = str(self.hoaEntry.get())

        # If/else statement to validate that all inputs are digits
        # first checks if all inputs are numbers and calls the get_tax_bill formula if they are
        # output appropriate message box indicating the mistake if either is false
        if (validrpv.isdigit() == TRUE) and (validhoa.isdigit() == TRUE):
            print("both statements confirmed true")
            self.calculate()
        elif validrpv.isdigit() == FALSE and (validhoa.isdigit() == TRUE):
            print("only rvp is false")
            messagebox.showerror("Conversion Error", "Property Value is not a valid number")
        elif validhoa.isdigit() == FALSE and (validrpv.isdigit() == TRUE):
            print("only hoa is false")
            messagebox.showerror("Conversion Error", "HOA Fee is not not a valid number")
        else:
            print("both inputs are false")
            messagebox.showerror("Conversion Error", "Neither of your inputs are valid numbers")

    #function used to delete entry fields when button is called
    def clear(self):
        print("inside CLEAR")
        self.rpvEntry.delete(0,END)
        self.hoaEntry.delete(0,END)

    # build the initial window interface
    def build(self):
        window = tk.Tk()
        window.minsize(400,150)
        window.maxsize(450, 170)
        window.title("Property Tax Calculator")
        
        # top label
        Label(window,text="""Property Tax Calculator""", fg='red', font=("Courier", 20), pady=10, padx=20).grid(row=0, column=0, columnspan=3)

        # create labels and entry fields
        Label(text="Real Property Value:", fg='blue').grid(row=1,column=0, sticky=E)
        self.rpvEntry = Entry(window)
        self.rpvEntry.grid(row=1,column=1, columnspan=2, padx=10, sticky=W)

        Label(text="HOA Fees:", fg='blue').grid(row=2, column=0, sticky=E)
        self.hoaEntry = Entry(window)
        self.hoaEntry.grid(row=2, column=1, columnspan=2, padx=10, sticky=W)

        # calculate button calls get_tax_bill when clicked
        self.calcButton = Button(window, text="Calculate", command=self.validate)
        self.calcButton.grid(row=3,column=0, padx=10, pady=10)

        # CLEAR button calls clear when clicked
        self.clearButton = Button(window, text="Clear", command=self.clear )
        self.clearButton.grid(row=3,column=1, padx=10, pady=10)

        # EXIT button calls closes app when clicked
        self.exitButton = Button(window, text="Exit", command=sys.exit )
        self.exitButton.grid(row=3,column=2, padx=10, pady=10)

        mainloop()

##     Here we go     ##
if __name__ == "__main__":
    bldr = Builder()
    bldr.build()