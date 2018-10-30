def countAppleAndOranges(s, t, a, b, apples, oranges):
    sam_apples = 0
    sam_oranges = 0

    for i in apples:
        if (a + i) in range(s, t + 1):
            sam_apples += 1

    for i in oranges:
        if (b - i) in range(s, t + 1):
            sam_oranges += 1
            
    print (sam_apples)
    print (sam_oranges)



    
s, t = 7, 11
a, b = 5, 15
apples = [-2, 2, 1]
oranges = [5, -6]

countAppleAndOranges(s, t, a, b, apples, oranges)
