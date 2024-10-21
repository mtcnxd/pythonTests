from tkinter import *
import serial # type: ignore
import requests # type: ignore

puerto = "/dev/ttyUSB0"
baudrate = 9600

class Pycalc(Frame):
	def __init__(self, master, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self.parent = master
		self.data = ""
		self.createWidgets()
		self.Port = serial.Serial(port=puerto, baudrate=baudrate, timeout=5)
		self.getTemperature()

	def createWidgets(self):
		labelTemperature = Label(text="Temperatura:")
		labelTemperature.place(x=10, y=10)
		
		self.entryTemperature = Entry(font=("Arial", 18), relief=RAISED, borderwidth=1)
		self.entryTemperature.place(x=10, y=30)
		self.entryTemperature.insert(0, "")

		labelAltitude = Label(text="Altitud:")
		labelAltitude.place(x=10, y=80)

		self.entryAltitude = Entry(font=("Arial", 18), relief=RAISED, borderwidth=1)
		self.entryAltitude.place(x=10, y=100)
		self.entryAltitude.insert(0, "")

		buttonPost = Button(text="Post Data", command=self.postData)
		buttonPost.place(x=10, y=150)

	def postData(self):
		url = "https://io.adafruit.com/api/v2/webhooks/feed/wCTd1eGUXzsVyVUT99TCRhh3qBpZ/raw"

		headers = {
    		'Content-Type': 'application/octet-stream'
		}

		requests.post(url, headers=headers, data=str(self.data[0]))

	def getTemperature(self):
		if self.Port.in_waiting > 0:
			byteResponse = self.Port.readline()
			stringResponse = byteResponse.decode().rstrip('\r\n')
			self.data = stringResponse.split(',')

			self.entryTemperature.delete(0, END)
			self.entryAltitude.delete(0, END)

			self.entryTemperature.insert(0, self.data[0] + " °C")
			self.entryAltitude.insert(0, self.data[1] + " meters")

		self.after(1000, self.getTemperature)


Termometer = Tk()
Termometer.title("Sensor BMP180")
Termometer.geometry('300x200')

root = Pycalc(Termometer)
Termometer.mainloop()
