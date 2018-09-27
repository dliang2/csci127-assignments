def collatz(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            print(int(n))
            steps += 1
        else:
            n = 3 * n + 1
            print(int(n))
            steps += 1
    return "Steps: " + str(steps)

print(collatz(9))
print(collatz(27))