#!/usr/bin/env	python3
def my_generator():
	print("Inside my generator")
	yield 'a'
	yield 'b'
	yield 'c'

if __name__ == '__main__':
	for char in my_generator():
		print(char)
