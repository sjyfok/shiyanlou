#!/usr/bin/env	python3
import sys

def mhour(minutes):
	h = 0
	m = 0
	if minutes < 59:
		m = minutes
	else:
		h, m = divmod(minutes, 60)		
	
	return h, m

if __name__ == '__main__':
	try:
		L = len(sys.argv)
		if int(sys.argv[L-1]) < 0:
			raise ValueError("Input number cannot be negative")
		else:
			(h, m) = mhour(int(sys.argv[L-1]))
			print("{} H, {} M".format(h, m))
	
	except ValueError:
		print("ValueError: Input number cannot be negative")
			
