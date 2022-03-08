from time import time,sleep
from random import randint

"""
Simple proportional–integral–derivative controller (PID) implementation
"""
class PID:
	def __init__(self, Kp, Ki, Kd, initTime=None):
		# if initTime isn't specified, use current epoch
		if initTime is None:
			initTime = time()

		### INPUT
		# Kp is the proportional gain
		self.Kp = Kp
		# Ki is the integral gain
		self.Ki = Ki
		# Kd is the derivative gain
		self.Kd = Kd

		### OUTPUT (Corrections)
		# Proportional correction
		self.Cp = 0.0
		# Integral correction
		self.Ci = 0.0
		# Derivative correction
		self.Cd = 0.0
		self.output = 0.0;

		self.prevTime = initTime
		self.prevError = 0.0

	def Update(self, error, currentTime=None):
		# if currentTime isn't specified, use current epoch
		if currentTime is None:
			currentTime = time()
		#  time derivative
		dt = currentTime - self.prevTime
		if dt <= 0.0:
			return 0
		# error derivative
		de = error - self.prevError

		# compute outputs with mathematical approximations
		self.Cp = error
		self.Ci += error * dt
		self.Cd = de / dt

		self.prevTime = currentTime
		self.prevError = error

		self.output = (self.Kp * self.Cp)    # proportional term
		+ (self.Ki * self.Ci)  # integral term
		+ (self.Kd * self.Cd)  # derivative term

		return self.output

def cruiseControl(desiredSpeed,numberOfIterations,Kp,Ki,Kd):
	# process variable (PV)
	currentSpeed = getCurrentSpeed()

	# get e(t)
	error = desiredSpeed - currentSpeed

	# compute PID
	pid = PID(Kp,Ki,Kd)

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