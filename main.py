#!/usr/bin/env python
import fermat_primality_test
import xorshift
def main():
	primes=[]
	xorgen = xorshift()
	while len(primes) < 10:
		num = xorgen()
		if fermat_test(num):
			primes.append(num)
	

if __name__ == '__main__':
	main()
