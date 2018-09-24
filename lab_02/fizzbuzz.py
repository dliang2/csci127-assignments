# Darren Liang
# Partner: Kyra Abbu

"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the
number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
Count how many times program returned "FizzBuzz"
"""

def fizzbuzz(max_value):
    count = 0 
    i = 1 # set up the loop
    while i <= max_value:
        if (i % 3 == 0) and (i % 5 == 0): # check if divisible by both
            count += 1 # add 1 to count if FizzBuzz occurs
            print("FizzBuzz")
        elif i % 3 == 0: # check if divisible by 3
            print("Fizz")
        elif i % 5 == 0: # check if divisible by 5
            print("Buzz")
        else: # if not divisible by 3 or 5
            print(i)
        i += 1 # makes sure that the loop will eventually end
    return "Count: " + str(count) # number of times FizzBuzz occurs

print(fizzbuzz(100)) # running print(function) displays the return value