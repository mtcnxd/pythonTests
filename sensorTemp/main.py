from machine import Pin, I2C, ADC
from time import sleep
from ssd1306 import SSD1306_I2C

led = Pin(25, Pin.OUT)
adc = ADC(4)
i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5))
oled = SSD1306_I2C(128, 32, i2c)

def ledBlink():
    led.value(1)
    sleep(0.1)
    led.value(0)

def getTemperature():
    ledBlink()
    temperature = adc.read_u16()
    temperature = temperature * 3.3 / 65535
    temperature = 27 - (temperature - 0.706)/0.001721
    return round(temperature, 1)

while True:
    temperature = getTemperature()
    print('Temperature: ' + str(temperature) + ' degrees')
    oled.fill(0)
    oled.text('Sensor: ' + str(temperature), 0, 0)
    oled.show()    
    sleep(5)

