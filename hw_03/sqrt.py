# Darren Liang and Stacey Li

def mysqrt(n):
    oldguess = 1 # random guess, can be any number except for 0
    while 1 > 0: # infinite loop
        newguess = ((oldguess + (n / oldguess)) / 2) # get closer to the answer
        print(n, oldguess)
        if newguess == oldguess: # break the infinite loop when we are satisfied with our answer
            break
        oldguess = newguess # makes oldguess the latest previous term
    return "Final Answer: " + str(newguess)


i = 1
while i <= 20: # print out the steps for the sqrt of numbers from 1 to 20
    print(mysqrt(i))
    i += 1