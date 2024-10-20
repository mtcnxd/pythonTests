from machine import Pin
import time
import math

sensor = Pin(8, Pin.IN)
led = Pin(13, Pin.OUT)

time_diff = 0
radio = 0.05
rpm = 0
values = []

def cumpute_rpm(rpm):
    ms = ((2 * math.pi) * (rpm)) * radio
    return ms * 3.6

def blink():
    led.on()
    time.sleep_ms(100)
    led.off()
    time.sleep_ms(100)


while True:
    int_clock = time.ticks_ms()
    
    if (sensor.value() == 1):
        rpm = rpm + 1
    
    if (time_diff < 1000):
        time.sleep_ms(1)
        time_diff += 1
        
    else :
        speed = cumpute_rpm(rpm)
        print("{0:.2f} K/h".format(speed))
        time_diff = 0
        rpm = 0