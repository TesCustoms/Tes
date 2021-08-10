#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-07"
__doc__     = "Class to ??"
"""
# Allow configuration of ???
# https://docs.micropython.org/en/latest/library/machine.html
from machine import Pin

# Interact with software I2C, hardware I2C, and OneWire serial intetfaces
# TODO
from machine import SoftI2C, I2C, onewire

# Allow interaction with capacitive touch pads
# TODO
from machine import TouchPad

# Small and fast JSON encoder and decoder for RESTful API communication
# https://pypi.org/project/ujson/
import ujson

# Allow interaction with O/S debugging and flash storage
# TODO
import esp
import uos

# Allow interaction with subsystem within ESP-32 module (e.g. Temp sensor)
# TODO
import esp32
from esp32 import NVS  # Non-volatile memory storage

import network
import ubluetooth

# Allow
# TODO
import time


MAX_CPU_FREQ = 240000000
HIGH = 1
LOW = 0
LASER_PIN = 0
TIME_HIGH_PULSE = 1
TIME_LOW_PULSE = 0

LASER_TIMEOUT = 0.001 # 1 ms = ?? meters in light Time Of Flight

def getDistance():

    # https://docs.micropython.org/en/latest/library/machine.html#machine.time_pulse_us
    machine.time_pulse_us(TesMufflerDrice.LASER_PIN, TIME_HIGH_PULSE, LASER_TIMEOUT)

TODO = -1

# Allow micropython to run on ESP-32
# https://docs.micropython.org/en/latest/esp32/tutorial/intro.html
# https://micropython.org/download/esp32

if __name__ == "__main__":
    machine.freq(MAX_CPU_FREQ)
    machine.soft_reset()
    machine.unique_id()




    # Available Pins are from the following ranges (inclusive): 0-19, 21-23, 25-27, 32-39. 
    # Pins 1 and 3 are REPL UART TX and RX respectively
    # Pins 6, 7, 8, 11, 16, and 17 are used for connecting the embedded flash, and are not recommended for other uses
    # Pins 34-39 are input only, and also do not have internal pull-up resistors
    # The pull value of some pins can be set to Pin.PULL_HOLD to reduce power consumption during deepsleep.
    
    ledPin = machine.Pin(0, machine.Pin.OUT, value=LOW) #GPIO0
    ledPin.on()
    ledPin.off()
    ledPin.value(HIGH)


    gpio_1 = Pin(1, Pin.IN, Pin.PUL_UP)
    print(gpio_1)
    
    time.sleep_us(10)   # 10 microseconds
    time.sleep_ms(5)    # 5 microseconds

    esp32.hall_senor()  # Model M magentic sensor
    esp32.ULP()         # Ultra low power co-processor 


    i2c = I2C(freq=400000)
    i2c.scan()

    i2c.writeto(42, b'123')         # write 3 bytes to slave with 7-bit address 42
    i2c.readfrom(42, 4)             # read 4 bytes from slave with 7-bit address 42

    i2c.readfrom_mem(42, 8, 3)      # read 3 bytes from memory of slave 42,
                                    #   starting at memory-address 8 in the slave
    i2c.writeto_mem(42, 2, b'\x10') # write 1 byte to memory of slave 42
                                    #   starting at address 2 in the slave
