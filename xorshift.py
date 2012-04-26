
class xorshift:
	def __init__(self):
		self.x = x = 123456789
		self.y = 362436069
		self.z = 521288629
		self.w = 88675123
	def __call__(self):
		t = self.x ^ (self.x<<11) & 0xffffffff
		self.x = self.y
		self.y = self.z
		self.z = self.w
		w = self.w
		self.w = (w ^ (w >> 19) ^(t ^ (t >> 8))) & 0xffffffff
		return self.w

xor = xorshift()
out = str(xor())
while len(out) < 100:
	out += str(xor())
print out
