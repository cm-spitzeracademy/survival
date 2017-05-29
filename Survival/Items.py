class Weapons(object):
	def __init__(self, type, power):
		self.type = type
		self.power = power

	def stats(self):
		print("Type %s" % self.type)
		print("Power %s" % self.power)
