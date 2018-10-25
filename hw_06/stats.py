# Darren Liang and Shanjida Kamal"

"""
100 items
value 1 to 10
1. find the largest (location of one of them)
2. frequency of a specific value
"""
import random

def build_random_list(size, max_value):
    l = []
    i = 0
    while i < size:
        l.append(random.randrange(0, max_value + 1))
        i += 1
    return l

l = build_random_list(100, 10)

def find_largest(l):
    highest = 0
    for num in l:
        if num > highest:
            highest = num
    return l.index(highest)

def frequency(value, l):
    return l.count(value)

print(l)
print(find_largest(l))
print(frequency(10, l))
    