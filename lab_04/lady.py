def isHappy(l, s):
    if l < 2 and s[0] == '_':
        return True
    if l == 2 and s[0] == s[1]:
        return True
    if l < 3:
        return False
    first = s[0]
    last = s[-1]
    for i in range(1, l):
        if s[i] != s[i - 1] or s[i] != s[i + 1]:
            return False
    if first != s[1] or last != s[-2]:
        return False
    return True
        
def buckets(s):
    chars = []
    vals = []
    for i in s:
        if i != '_':
            if i not in chars:
                chars += [i]
                vals += [1]
            else:
                vals[chars.index(i)] += 1
    return vals

def check (l, s):
    if isHappy(l, s):
        pass
    elif '_' in s:
        vals = buckets(s)
        for i in vals:
            if i < 2:
                return "NO"
    return "YES"
    
def happyLadybugs(g1_size, g1_info, g2_size, g2_info, g3_size, g3_info, g4_size, g4_info):
    print(check(g1_size, g1_info))
    print(check(g2_size, g2_info))
    print(check(g3_size, g3_info))
    print(check(g4_size, g4_info))

g1_size = 7
g1_info = "RBY_YBR"
g2_size = 6
g2_info =" X_Y__X"
g3_size = 2
g3_info = "__"
g4_size = 6
g4_info = "B_RRBR"

happyLadybugs(g1_size, g1_info, g2_size, g2_info, g3_size, g3_info, g4_size, g4_info)
