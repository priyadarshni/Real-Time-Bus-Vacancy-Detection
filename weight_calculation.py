#!/usr/bin/env python
from interfacing import interfacing

"""
consider average weight as 60kg.. in the prototype 60kg= 1000g i.e 1g=0.06kg

"""

inf = interfacing()

def calculate_vacancy(weight):
	if (weight >= 400):
		print "no vacant seat"
		return 0
	elif (weight < 400 and weight >= 300 ):
		print “1 vacant seat”
		return 1
	elif (weight < 300 and weight >= 200):
		print “2 vacant seat”
		return 2
	elif (weight < 200 and weight >= 100):
		print “3 vacant seat”
		return 3
	elif(weight < 50)
		print “4 vacant seat”
		return 4

def get_seat_vacancy():
	vacancy=0;
	vacancy+=calculate_vacancy(inf.weight1)
	vacancy+=calculate_vacancy(inf.weight2)
	vacancy+=calculate_vacancy(inf.weight3)
	vacancy+=calculate_vacancy(inf.weight4)
	print vacancy, " seats vacant"
	return vacancy

"""
if the bus seats are full then the weight will be approx 60*no of seats.
in the prototype, it will be 1000g*16=16000g ie 16 kg.
and considering that approximately 20 people can stand.. the weight of entire bus will be 16kg+20kg=36kg
consider weight of bus chasis as 500g i.e 36500g
"""
def get_standing_vacancy():
	total_weight = inf.weight5 #weight of entire bus, weight by 40kg sensor
	if (total_weight >= 3650):
		print “bus full! no standing vacancy”
		return 0
	elif (total_weight < 3650 and total_weight >= 2500 ):
		print “50% standing vacancy”
		return 50
	elif(total_weight < 2500 and total_weight >= 2000)
		print “75% standing vacancy”
		return 75
	elif(weight < 2000)
		print “full standing vacancy”
		return 100
	

if __name__ == "__main__":

    setup()
    
    inf.get_readings()
    get_seat_vacancy()
    get_standing_vacancy()

