import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711


class interfacing:

def __init__(self):

	self.load1 = HX711(5, 6); #pin assignment according to one's favourite
"""	self.load2 = HX711(9, 11); #pin assignment according to one's favourite
	self.load3 = HX711(17, 27); #pin assignment according to one's favourite
	self.load4 = HX711(19, 26); #pin assignment according to one's favourite
	self.load5 = HX711(20, 21); #pin assignment according to one's favourite"""

	self.calibration_factor_1 = 30.25; #please calibrate according to your load cell
"""	self.calibration_factor_2 = -375;  #please calibrate according to your load cell
	self.calibration_factor_3 = -375;  #please calibrate according to your load cell
	self.calibration_factor_4 = -375;  #please calibrate according to your load cell
	self.calibration_factor_5 = -375;  #please calibrate according to your load cell"""

	self.weight1 = 0 #weight from sensor 1
	self.weight2 = 0 #weight from sensor 2
	self.weight3 = 0 #weight from sensor 3
	self.weight4 = 0 #weight from sensor 4
	self.weight5 = 0 #weight from sensor 5

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

def setup():
    """
    code run once
    """
    self.load1.set_offset(8389020)
    self.load1.set_scale(calibration_factor_1)
    """
    self.load2.set_offset(8389020)
    self.load2.set_scale(calibration_factor_2)
    self.load3.set_offset(8389020)
    self.load3.set_scale(calibration_factor_3)
    self.load4.set_offset(8389020)
    self.load4.set_scale(calibration_factor_4)
    self.load5.set_offset(8389020)
    self.load5.set_scale(calibration_factor_5)
"""
pass


#reads weight from load cell 
def read_readings(load):
	weight=0
	try:
	   for i in range(10):
		weight+=self.load.get_weight()
 		load.power_down()
           	time.sleep(.001)
	   	load.power_up()
	   return weight/10
	  
	except (KeyboardInterrupt, SystemExit):
	   cleanAndExit()

#gets reading from all load cells
def get_readings(self):
	self.weight1 = read_readings(self.load1)
	print "load cell 1: ",self.weight1
	#weight2 = read_readings(load2)
	print "load cell 2: ",self.weight2
	#weight3 = read_readings(load3)
	print "load cell 3: ",self.weight3
	#weight4 = read_readings(load4)
	print "load cell 4: ",self.weight4
	#weight5 = read_readings(load5)
	print "load cell 5: ",self.weight5


