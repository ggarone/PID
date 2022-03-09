from time import sleep
from random import randint
import PID

def cruiseControl(desiredSpeed,numberOfIterations,Kp,Ki,Kd):
	# process variable (PV)
	currentSpeed = getCurrentSpeed()

	# get e(t)
	error = desiredSpeed - currentSpeed

	# compute PID
	pid = PID.PID(Kp,Ki,Kd)

	# updates PID for n numberOfIterations
	for i in range(1,numberOfIterations):
		currentSpeed = getCurrentSpeed(int(currentSpeed))
		error = desiredSpeed - currentSpeed
		correction = pid.Update(error)
		setSpeed(correction)
		currentSpeed += correction
		print(f'Speed correction: {correction:0.3f} e(t): {error:0.3f} currentSpeed: {currentSpeed:0.3f}')
		sleep(1)

"""
this function simulates output from a Tachometer 
simulation is done by randomly increasing or decreasing the speed by 5 km/h 
(seems a reasonable assumption since the cruise control checks the car's speed once per second)
"""
def getCurrentSpeed(prevSpeed=None):
	if prevSpeed is None:
		speed = randint(60,110)
	else:
		speed = randint(prevSpeed-5,prevSpeed+5);
	return speed

# this function will simulate a call to the car hw that actually control its speed
def setSpeed(speed):
	pass

if __name__ == '__main__':
	# Possible usage of a PID: Cruise Control
	# A cruise control is a system that takes over the throttle of the car to maintain a steady speed previously set by the driver
	######################
	#   CRUISE CONTROL   #
	######################

	"""USER INPUTS"""
	# desired setpoint (SP)
	desiredSpeed = 90  # in km/h
	# gains
	Kp = 0.5
	Ki = 0.2
	Kd = 0.01
	# number of iteration before the program stops (one iteration per second)
	numberOfIterations = 100

	cruiseControl(desiredSpeed,numberOfIterations,Kp,Ki,Kd)