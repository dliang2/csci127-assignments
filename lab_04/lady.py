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
    if (first != s[1] or last != s[-2]):
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
    
def happyLadybugs(game1, game1_info, game2, game2_info, game3, game3_info, game4, game4_info):
    print(check(game1, game1_info))
    print(check(game2, game2_info))
    print(check(game3, game3_info))
    print(check(game4, game4_info))

game1 = 7
game1_info = "RBY_YBR"
game2 = 6
game2_info =" X_Y__X"
game3 = 2
game3_info = "__"
game4 = 6
game4_info = "B_RRBR"

happyLadybugs(game1, game1_info, game2, game2_info, game3, game3_info, game4, game4_info)
