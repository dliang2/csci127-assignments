# Darren Liang and Shanjida Kamal"

"""
100 items
value 1 to 10
1. find the largest (location of one of them)
2. frequency of a specific value
3. mode
"""
import random

def build_random_list(size, max_value):
    l = []
    for i in range(size):
        l.append(random.randrange(1, max_value + 1))
    return l

l = build_random_list(100, 10)

def index_largest(l):
    highest = l[0]
    for num in l:
        if num > highest:
            highest = num
    return l.index(highest)

def frequency(value, l):
    return l.count(value)

def mode(l):
    test_mode = l[0] # initial mode is first number of the list
    max_value = l[index_largest(l)] # highest number of list
    for i in range(0, max_value + 1): # go through list from 1 to highest number
        if frequency(test_mode, l) < frequency(i + 1, l): # compare modes
            test_mode = i + 1 # if number has higher freq count, becomes mode
    mode = test_mode
    return mode
        
def bucket_mode(l, max_value):
    tallies = []
    for i in range(max_value): # create 10 buckets
        tallies.append(0) # each bucket starts at 0 count
    for item in l: # add a count to their respective tally bucket
        tallies[item] = tallies[item] + 1 
    li = index_largest(tallies)
    return li
    
print(l)
print("Index of Largest:", index_largest(l))

for i in range(1, l[index_largest(l)] + 1):
    print("Frequency of " + str(i) + ":", frequency(i, l))

print("Mode:", mode(l))
print("Frequency of Mode:", frequency(mode(l), l))

print("Mode:", bucket_mode(l, l[index_largest(l)] + 1))
print("Frequency of Mode:", frequency(bucket_mode(l, l[index_largest(l)] + 1), l))