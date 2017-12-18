#!/usr/bin/env	python3

class Counter(object):
	def __init__(self, low, high):
		self.low = low
		self.high = high
	def __iter__(self):
		counter = self.low
		while self.high >= counter:
			yield counter
			counter += 1

if __name__ == '__main__':
	gobj = Counter(5, 10)
	for num in gobj:
		print(num, end = " ")

	print()
	for num in gobj:
		print(num, end = ' ')

