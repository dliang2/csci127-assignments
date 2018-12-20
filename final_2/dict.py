def addline(d, line):
    line = line.lower()
    for word in line.split():
        if word[0] not in d:
            d[word[0]] = [word]
        elif word not in d[word[0]]:
            d[word[0]].append(word)
    return d

d = {
    "o": ["one"],
    "t": ["two", "three"],
    "s": ["seven"]
    }
print(d)
print("------------------------------")
addline(d, "down the rockefeller street")
addline(d, "keep moving if you want to know what the rockefeller groove is")
addline(d, "the daylight is fading away")
addline(d, "it is show time in the middle of the street lights")
addline(d, "everything is all but surreal")
print(d)

def spellcheck(d, word):
    word = word.lower()
    if word[0] in d:
        if word in d[word[0]]:
            return True
    return False
print("------------------------------")
print(spellcheck(d, "rockefeller"))
print(spellcheck(d, "okay"))
print(spellcheck(d, "hello"))
