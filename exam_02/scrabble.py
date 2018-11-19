def score(w):
    w = w.lower()
    chars = []
    for letter in w:
        chars.append(letter)
    score = 0
    for char in chars:
        if char in "aeioulnrst":
            score += 1
        elif char in "dg":
            score += 2
        elif char in "bcmp":
            score += 3
        elif char in "fhvwy":
            score += 4
        elif char in "k":
            score += 5
        elif char in "jx":
            score += 8
        else:
            score += 10
    return score

print(score("hello"))