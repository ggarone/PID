from time import time

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