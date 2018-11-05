"""
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
"""

def isHappy(l, s):
    if l < 3:
        if l == 0:
            return False
        elif l == 1 and s[0] == '_':
            return True
        elif l == 2 and s[0] == s[1]:
            return True
        else:
            return False
    else:
        vals = dict(s).values()
        if min(vals) < 2:
            return False
    return True
        
def dict(s):
    d = {}
    for i in s:
        if i != '_':
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    return d

def check (l, s):
    if isHappy(l, s):
        return "YES"
    else:
        return "NO"

def happyLadybugs(size, info):
    return check(size, info)

g1_size = 7
g1_info = "RBY_YBR"
g2_size = 6
g2_info =" X_Y__X"
g3_size = 2
g3_info = "__"
g4_size = 6
g4_info = "B_RRBR"

print(happyLadybugs(g1_size, g1_info))
print(happyLadybugs(g2_size, g2_info))
print(happyLadybugs(g3_size, g3_info))
print(happyLadybugs(g4_size, g4_info))

