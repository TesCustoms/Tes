#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-07"
__doc__     = "Class to ??"
"""
TODO = -1  
# https://micropython.org/download/esp32

# Allow micropython to run on ESP-32
# https://docs.micropython.org/en/latest/esp32/tutorial/intro.html

# Allow configuration of CPU setting
# 
import machine 

import time 
import utime 


MAX_CPU_FREQ = 240000000

if __name__ == "__main__":
    machine.freq(MAX_CPU_FREQ)
    ledPin = machine.Pin(25, machine.Pin.OUT)