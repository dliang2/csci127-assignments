def cake(A, B, u):
    slice = A / B # units of cake
    slice_count = u / slice # how many slices available
    invite_count = int(slice_count) # never round up
    return invite_count
    
print(cake(5, 10, 1)) # expect 2
print(cake(10, 5, 7)) # expect 3
print(cake(7, 4, 9)) # expect 5