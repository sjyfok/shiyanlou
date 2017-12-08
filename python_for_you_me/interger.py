#!/usr/bin/env python3

days = int(input("Enter days: "))
tmp = days
months = days//30
days = days%30
print("Months = {} Days = {}".format(months,days))
days = tmp
#divmod(num1, num2) = (d, r)  d = num1//num2, r = num1%num2
print("Months = {} Days = {}".format(*divmod(days, 30)))

