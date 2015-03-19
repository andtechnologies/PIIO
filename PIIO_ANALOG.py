#!/usr/bin/python
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0) # For CS 0
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def readchannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def convertvolts(data,volt,places):
  volts = (data * volt) / float(1023)
  volts = round(volts,places)
  return volts
 
 
# Main code

while True:
 
  level = readchannel(0)
  voltage = convertvolts(level,5,2)
  
 
  # Print out results
  print "--------------------------------------------"
  print("Light:" voltage)
 
 
  # Wait before repeating loop
  time.sleep(5)
