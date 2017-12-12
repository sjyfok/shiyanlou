#!/usr/bin/env python3

outs=''
f = open('/home/shiyanlou/Code/String.txt')
ins = f.read()

for c in ins:
	if c.isdigit():
		outs += c

print(outs)
