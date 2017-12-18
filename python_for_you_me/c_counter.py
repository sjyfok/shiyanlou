#!/usr/bin/env python3

class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.high:
            raise  StopIteration
        else:
            self.current += 1
            return self.current -1

if __name__ == '__main__':
    c = Counter(5, 10)
    for i in c:
        print(i, end = " ")


