#!/usr/bin/env	python3
import math

def longest_side(a, b):
	"""
	aaaa
	bbbb
	"""
	return math.sqrt(a*a + b*b)

if __name__ == '__main__':
	print(longest_side.__doc__)
	print(longest_side(4, 5))

