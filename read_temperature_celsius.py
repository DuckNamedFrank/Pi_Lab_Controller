#!/usr/bin/python

import smbus
import time
import datetime

bus = smbus.SMBus(1)

#I2C addres
address = 0x4d
 
 
def get_celsius_val(): 
	data = bus.read_i2c_block_data(address, 1,2)
	val = (data[0] << 8) + data[1]
	return val/5.00


while 1 == 1:
	temperature = get_celsius_val()
	print temperature
	time.sleep(1)
