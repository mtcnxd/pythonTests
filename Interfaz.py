from tkinter import *
import requests # type: ignore
import json

class Window(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.counter = 0
		self.varname = StringVar()
		self.createWidgets()
		self.increment()

	def createWidgets(self):
		labelValue = Label(text="Sensor Value:")
		labelValue.place(x=10,y=10)

		self.sensorValue = Entry()
		self.sensorValue.place(x=10, y=30)

		buttonReset = Button(text="Reset", command=self.resetValue)
		buttonReset.place(x=10, y=60)

		self.textValue = Entry()
		self.textValue.place(x=160, y=30)

		buttonReset = Button(text="Read File", command=self.readFile)
		buttonReset.place(x=120, y=60)

		self.requestName = Entry(textvariable=self.varname)
		self.requestName.place(x=10, y=150)

		self.requestEmail = Entry()
		self.requestEmail.place(x=10, y=180)		

		buttonReset = Button(text="Get Request", command=self.getResponse)
		buttonReset.place(x=220, y=60)

		buttonSend = Button(text="Post Request", command=self.postRequest)
		buttonSend.place(x=10, y=220)

	def increment(self):
		self.counter += 1
		self.sensorValue.delete(0, END)
		self.sensorValue.insert(0, str(self.counter))
		self.after(500, self.increment)

	def resetValue(self):
		print(self.varname.get())
		self.counter = 0
		self.sensorValue.delete(0, END)
		self.textValue.delete(0, END)
		self.requestName.delete(0, END)
		self.requestEmail.delete(0, END)
		self.sensorValue.insert(0, self.counter)

	def readFile(self):
		try:
			file = open("hola.txt")
			text = file.read().rstrip()
			file.close()			
		except FileNotFoundError:
			text = "File not found!" 
			print(text)

		self.textValue.delete(0, END)
		self.textValue.insert(0, text)			

	def getResponse(self):
		url = "https://jsonplaceholder.typicode.com/users/1"
		response = requests.get(url)
		print(response.text)

		jsonObj = json.loads(response.text)
		self.requestName.delete(0, END)
		self.requestName.insert(0, jsonObj["name"])

		self.requestEmail.delete(0, END)
		self.requestEmail.insert(0, jsonObj["email"])

	def postRequest(self):
		url = "https://io.adafruit.com/api/v2/webhooks/feed/wCTd1eGUXzsVyVUT99TCRhh3qBpZ/raw"

		headers = {
    		'Content-Type': 'application/octet-stream'
		}

		print(self.counter)
		requests.post(url, headers=headers, data=str(self.counter))


MainWindow = Tk()
MainWindow.title("Sensor BM180")
MainWindow.geometry("400x400")

Window(MainWindow)

MainWindow.mainloop()