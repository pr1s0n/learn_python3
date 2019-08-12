class Animal(object):
	def __init__(self):
		print('this is an Animal!')

class Runable(object):
	def run(self):
		print('Running...')

class Flyable(Animal):
	def fly(self):
			print('Flying...')

class Dog(Animal,Runable):
		def dog(self):
			return print('dog')
dogs = Dog()
dogs.run()
dogs.dog()