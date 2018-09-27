# Darren Liang and Stacey Li

def mysqrt(n):
    i = 1
    oldguess = 1
    while i > 0:
        newguess = ((oldguess + (n / oldguess)) / 2)
        print(n, oldguess)
        if newguess == oldguess:
            break
        oldguess = newguess
    return newguess


i = 1
while i <= 20:
    print(i, mysqrt(i))
    i += 1