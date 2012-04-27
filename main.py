#!/usr/bin/env python
from fermat_primality_test import fermat_test
import xorshift
from time import time
import sys
'''
Most of the commands here are just to calculate stats and print
out to the user, no hard logic to understand (=
'''
def output(a,b,c):
	print a,b,c
def main():
	global output #Bringing to local scope
	if not(len(sys.argv)>1 and sys.argv[1] == '--verbose'):
		output=lambda a,b,c:0 
		print 'Generating...'
		
	primes=[]
	xorgen = xorshift.xorshift100()
	fermat = fermat_test()

	ttotalstart=time()
	totalxor=0
	totalfermat=0
	tries=0
	while len(primes) < 10:
		tries+=1
		txor = time()
		num = xorgen()
		x = -txor+time()
		totalxor+=x
		output( 'Generated a 100 digit random number in', x, 'seconds.')
		tfermat=time()
		if fermat(num):
			primes.append(num)
		f = -tfermat+time()
		totalfermat+=f
		output( 'Fermat test spent', f, 'seconds.')

	total = time() - ttotalstart
	print '\nTotal time elapsed:', total, 'seconds.'
	print 'Total spent by Fermat:', totalfermat, 'seconds.'
	print 'Total spent by xorshift:', totalxor, 'seconds.'

	print '\n'+str(int((totalxor/total)*100))+'% of time was elapsed in xorshift100.'
	print 'Fermat test detected', tries-10, 'non-primes.'

	print '\nPrinting the 10 (probable) primes generated:'
	for p in primes:
		print p
	
if __name__ == '__main__':
	main()
