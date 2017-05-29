class Villager(object):
	def __init__(self, name, strength, defense, life):
		self.name = name
		self.strength = strength
		self.defense = defense
		self.life = life

	def add_strength(self, amount):	
		self.strength = self.strength + amount

	def remove_strength(self):
		pass

	def add_defense(self, amount):
		self.defense = self.defense + amount

	def remove_defense(self):
		pass

	def add_life(self, amount):
		self.life = self.life + amount

	def remove_life(self, amount):
		self.life = self.life - amount

	def stats(self):
		print("Name: %s" % self.name)
		print("Strength: %s" % self.strength)
		print("Defense: %s" % self.defense)
		print("Life: %s" % self.life)
