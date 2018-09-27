# Darren Liang and Stacey Li

def collatz(n):
    steps = 0 # placeholder to count amount of steps
    while n != 1: # keep looping until n equal to 1
        if n % 2 == 0: # divide by 2 if even
            n = n / 2
            print(int(n)) # remove decimals
            steps += 1 # add 1 step
        else: # multiply by 3 and add 1 if odd
            n = (3 * n) + 1
            print(int(n))
            steps += 1 
    return "Steps: " + str(steps)

print(collatz(9))
print(collatz(27))