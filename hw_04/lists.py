# Darren Liang and Emily Fang

import random
def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the list
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l

def locate(l, value): # returns the first appearance
    i = 0
    while i < len(l): # go through the list until you find the value
        if l[i] == value:
            return i # the value has been found
        else:
            i += 1
    return -1 # the loop did not find the value, so it should return -1

def count(l, value):
    i = 0
    counter = 0
    while i < len(l): # loop through the entire list
        if l[i] == value:
            counter += 1 # add 1 to counter when a value is found
        i += 1
    return counter # number of times the value appears

def reverse(l):
    return l[::-1] # return the entire list, but in every -1 step. aka backwards

def isIncreasing(l):
    i = 0
    while i < len(l) - 1: # length needs to be minus 1, because 
        if l[i] < l[i + 1]: # l[i + 1] will be the last number to be checked
            i += 1
        else:
            return False
    return True

def palindrome(l): # palindrome means the lists should be the same when reversed
    return l == reverse(l)
    

l = [1, 3, 5, 7, 11, 13, 17]
l2 = [7, 7, 4, 1 , 0, 0, 1, 4, 7, 7]

#print(build_random_list(5, 100))

print(locate(l, 4)) # should return -1
print(locate(l2, 1)) # should return 3

print(count(l, 3)) # should return 1
print(count(l2, 7)) # should return 4

print(reverse(l))
print(reverse(l2))

print(isIncreasing(l)) # should return True
print(isIncreasing(l2)) # should return False

print(palindrome(l)) # should return False
print(palindrome(l2)) # should return True    
    