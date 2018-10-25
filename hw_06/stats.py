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
        l.append(random.randrange(1, max_value + 1))
        i += 1
    return l

l = build_random_list(100, 10)

def find_largest(l):
    highest = l[0]
    for num in l:
        if num > highest:
            highest = num
    return l.index(highest)

def frequency(value, l):
    return l.count(value)

def mode(l):
    mode = l[0]
    i = 0
    num = 1
    while i < 9:
        if frequency(num, l) < frequency(num + 1, l):
            mode = i
        num += 1
        i += 1
    return mode   

print(l)
print("Index of Largest:", find_largest(l))
print("Frequency of 5:", frequency(5, l))
print("Frequency of 7:", frequency(7, l))
print("Mode:", mode(l))
print("Frequency of Mode:", frequency(mode(l), l))