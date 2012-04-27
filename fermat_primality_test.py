from random import random
class fermat_test:
	def __init__(self, k = 100):
		self.k = k # number of tries
	def set_num_tests(self, x):
		self.k = x

	def __call__(self, x):
		for _ in range(self.k):
			r=int(random()*x)
			if x%2==0 or pow(r, x-1, x) != 1: #Modular Expo
				return False
		return True #probable prime
		
