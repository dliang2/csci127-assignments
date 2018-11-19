def encode(s):
    l = [[s[0]]]
    for i in range(len(s) - 1):
        if s[i] != s[i - 1]:
            l.append([s[i]])
        else:
            pass
    counts = []
    for count in range(len(l)):
        counts.append(0)
        
    # insert counting mechanism here
        
    for num in range(len(counts)):
        l[num].append(num)
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