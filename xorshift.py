from random import seed
from random import random
from time import time
class xorshift:
	def __init__(self):
		# By default, seed is already the system time
		seed(time()) # Change the seed
		maxi = 2**32 - 1
		self.x = int(random()*maxi)
		self.y = int(random()*maxi)
		self.z = int(random()*maxi)
		self.w = int(random()*maxi)
	def __call__(self):
		seed(time()) # Change the seed
		t = self.x ^ (self.x<<11) & 0xffffffff # Make sure it is under 32 bits.
		self.x = self.y
		self.y = self.z
		self.z = self.w
		w = self.w
		self.w = (w ^ (w >> 19) ^(t ^ (t >> 8))) & 0xffffffff
		return self.w


class xorshift100:
	def __init__(self):
		self.xors=[]
		for _ in range(11): #Each xorshift output a number 8-10 digits long (decimal)
			self.xors.append(xorshift())

	def __call__(self):
		st=''
		while len(st)<100: #should iterate just once
			for x in self.xors:
				st+=str(x())
		#kill less significant chars after the 100th
		st = st[:100]

		return int(st)
