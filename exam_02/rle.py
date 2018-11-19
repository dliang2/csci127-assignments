def encode(s):
    l = []
    count = 1
    for i in range(0, len(s) - 1):
        if s[i] != s[i + 1]:
            l.append([s[i], count])
            count = 1 # reset count
        else:
            count += 1
        last = [s[i], count]
    l.append(last)
    return l
    
print(encode("abbaaacddaaa"))
print(encode("abcd"))
print(encode("cbbbbbdee"))

print('--------------------------------------------------')

def decode(l):
    s = ""
    for pair in l:
        s += pair[0] * pair[1]
    return s

print(decode([['a', 1], ['b', 2], ['a', 3], ['c', 1], ['d', 2], ['a', 3]]))
print(decode([['a', 1], ['b', 1], ['c', 1], ['d', 1]]))
print(decode([['c', 1], ['b', 5], ['e', 2]]))