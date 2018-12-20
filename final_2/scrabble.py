def canMakeWord(letters, word):
    for letter in word:
        if letter in letters:
            i = letters.index(letter)
            letters = letters[:i] + letters[i + 1:]
        else:
            return False
    return True

print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriin","eerie"))
print(canMakeWord("orrpgma","program"))
print(canMakeWord("orppgma","progrm"))

def withWild(letters, word):
    for letter in word:
        if letter in letters:
            if "?" in letters:
                i = letters.index("?")
                letters = letters[:i] + letters[i + 1:]
            else:
                i = letters.index(letter)
                letters = letters[:i] + letters[i + 1:]
        else:
            return False
    return True

print("-------------------------")
print(withWild("ladilmy","daily"))
print(withWild("ee?rriin","eerie")) # needs one wild card
print(withWild("orrpgma","program"))
print(withWild("?orppgma?","progrm")) # needs two wild cards