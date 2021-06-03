from tkinter import *
from tkinter import messagebox

calculator = Tk()
p1 = PhotoImage(file = 'logo.png')
calculator.iconphoto(False, p1)

calculator.title("NILESH CALCULATOR")
calculator.geometry('400x570')

class Application(Frame):
	def __init__(self, master, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self.createWidgets()

	def replaceText(self, text):
		self.display.delete(0, END)
		self.display.insert(0, text)

	def appendToDisplay(self, text):
		self.entryText = self.display.get()
		self.textLength = len(self.entryText)

		if self.entryText == "0":
			self.replaceText(text)
		else:
			self.display.insert(self.textLength, text)

	def calculateExpression(self):
		self.expression = self.display.get()
		self.expression = self.expression.replace("%", "/ 100")

		try:
			self.result = eval(self.expression)
			self.replaceText(self.result)
		except:
			messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=calculator)

	def clearText(self):
		self.replaceText("0")

	def createWidgets(self):
		self.display = Entry(self, font=("Helvetica", 20), insertwidth=10, borderwidth=2, bg="red", relief=RAISED, justify=RIGHT)
		self.display.insert(0, "0")
		self.display.grid(padx=15, pady=15, ipadx = 30, ipady = 35, row=0, column=0, columnspan=4)

	
		self.plusButton = Button(self, font=("Helvetica", 20), text="+", borderwidth=2, bg="lime", command=lambda: self.appendToDisplay("+"))
		self.plusButton.grid(ipady=15,row=1, column=0, sticky="NWNESWSE")

		self.minusButton = Button(self, font=("Helvetica", 20), text="-", borderwidth=2, bg="lime", command=lambda: self.appendToDisplay("-"))
		self.minusButton.grid(ipady=15, row=1, column=1, sticky="NWNESWSE")
		
		self.timesButton = Button(self, font=("Helvetica", 20), text="*", borderwidth=2, bg="lime", command=lambda: self.appendToDisplay("*"))
		self.timesButton.grid(ipady=15, row=1, column=2, sticky="NWNESWSE")

		self.divideButton = Button(self, font=("Helvetica", 20), text="/", borderwidth=2, bg="lime", command=lambda: self.appendToDisplay("/"))
		self.divideButton.grid(ipady=15, row=1, column=3, sticky="NWNESWSE")

		

		self.sevenButton = Button(self, font=("Helvetica", 20), text="7", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("7"))
		self.sevenButton.grid(ipady=15, row=2, column=0, sticky="NWNESWSE")

		self.eightButton = Button(self, font=("Helvetica", 20), text="8", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("8"))
		self.eightButton.grid(ipady=15, row=2, column=1, sticky="NWNESWSE")

		self.nineButton = Button(self, font=("Helvetica", 20), text="9", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("9"))
		self.nineButton.grid(ipady=15, row=2, column=2, sticky="NWNESWSE")
	
		self.percentageButton = Button(self, font=("Helvetica", 20), text="%", borderwidth=2, bg="lime", command=lambda: self.appendToDisplay("%"))
		self.percentageButton.grid(ipady=15, row=2, column=3, sticky="NWNESWSE")


		

		self.threeButton = Button(self, font=("Helvetica", 20), text="4", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("4"))
		self.threeButton.grid(ipady=15, row=3, column=0, sticky="NWNESWSE")

		self.fiveButton = Button(self, font=("Helvetica", 20), text="5", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("5"))
		self.fiveButton.grid(ipady=15, row=3, column=1, sticky="NWNESWSE")

		self.sixButton = Button(self, font=("Helvetica", 20), text="6", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("6"))
		self.sixButton.grid(ipady=15, row=3, column=2, sticky="NWNESWSE")

		self.clearButton = Button(self, font=("Helvetica", 20), text="C", borderwidth=2, bg='yellow', command=lambda: self.clearText())
		self.clearButton.grid(ipady=15, row=3, column=3, sticky="NWNESWSE")

		
		
              
		self.twoButton = Button(self, font=("Helvetica", 20), text="1", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("1"))
		self.twoButton.grid(ipady=15, row=4, column=0, sticky="NWNESWSE")

		self.twoButton = Button(self, font=("Helvetica", 20), text="2", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("2"))
		self.twoButton.grid(ipady=15, row=4, column=1, sticky="NWNESWSE")

		self.threeButton = Button(self, font=("Helvetica", 20), text="3", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("3"))
		self.threeButton.grid(ipady=15, row=4, column=2, sticky="NWNESWSE")

		self.equalsButton = Button(self, font=("Helvetica", 20), text="=", borderwidth=2, bg='white', command=lambda: self.calculateExpression())
		self.equalsButton.grid(ipady=15, row=4, column=3, sticky="NWNESWSE", rowspan=2)





		self.threeButton = Button(self, font=("Helvetica", 20), text=".", borderwidth=2, bg='gray', command=lambda: self.appendToDisplay("."))
		self.threeButton.grid(ipady=15, row=5, column=0, sticky="NWNESWSE")

		self.zeroButton = Button(self, font=("Helvetica", 20), text="0", borderwidth=2, bg='cyan', command=lambda: self.appendToDisplay("0"))
		self.zeroButton.grid(ipady=15, row=5, column=1, sticky="NWNESWSE")

		self.clearButton = Button(self, font=("Helvetica", 20), text="AC", borderwidth=2, bg='yellow', command=lambda: self.clearText())
		self.clearButton.grid(ipady=15, row=5, column=2, sticky="NWNESWSE")
		


app = Application(calculator).grid()		
calculator.mainloop()
