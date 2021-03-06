#!/usr/bin/env python3
import sys
from collections import Counter


class Person(object):
	def __init__(self,  grade):
		self.grade = grade
	
	def get_grade(self) :
		return self.grade


class Student(Person):
	def __init__(self, grade):
        	Person.__init__(self, grade)

	def get_grade(self):
		c = Counter(self.grade)
		c.most_common(4)
		s = ''.join(sorted(c.elements()))
		L = len(s)
		pos = s.find('D')
		print("Pass: {}, Fail: {}".format(pos, L-pos))
	

class Teacher(Person):
	def __init__(self, grade):
		Person.__init__(self, grade)
	def get_grade(self):
		t = Counter(self.grade).most_common(4)
		L = len(t)
		i = 0
		while i < (L-1):
			print("{}: {}".format(t[i][0], t[i][1]), end = ', ')
			i += 1
		print("{}: {}".format(t[L-1][0], t[L-1][1]))
		 

if __name__ == '__main__':
	if sys.argv[1] == 'teacher':
		teacher1 = Teacher(sys.argv[2])
		teacher1.get_grade()
	if sys.argv[1] == 'student':
		student1 = Student(sys.argv[2])
		student1.get_grade()

