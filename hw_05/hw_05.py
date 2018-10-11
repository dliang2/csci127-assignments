def filterodd(l):
    new_list = []
    for i in l:
        if i % 2 != 0:
            new_list += [i]
    return new_list

print(filterodd([1, 2, 3, 4, 5, 6, 7, 8])) # should return [1, 3, 5, 7]
            
def mapsquare(l):
    new_list = []
    for i in l:
        new_list += [i*i]
    return new_list

print(mapsquare([4, 2, 5, 3, 5])) # should return [16, 4, 25, 9, 25]