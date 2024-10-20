from machine import ADC, Pin
from neopixel import NeoPixel
import random
import time

adc = ADC(Pin(26))
pin = Pin(23, Pin.OUT)
np  = NeoPixel(pin, 1)

while True:
    value = adc.read_u16()
    print("ADC value:" + str(value))  
    np[0] = (0,0,1)
    np.write()
    time.sleep_ms(1000)
    
    