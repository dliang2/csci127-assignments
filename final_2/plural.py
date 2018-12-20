def countPlurals(line):
    count = 0
    for word in line.split():
        if word[-1] == "s":
            count += 1
    return count

print(countPlurals("there are so many things to do ladybugs"))
print(countPlurals("the line will not have many plurals"))

def notPossessive(line):
    count = 0
    for word in line.split():
        if word[-1] == "s" and word[-2] != "'":
            count += 1
    return count

print(notPossessive("gorillas gorilla's cats"))
print(notPossessive("a dog's toys"))