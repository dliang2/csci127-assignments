def makeacronym(s):
    acronym = []
    s = s.lower()
    word_list = s.split(' ')
    for word in word_list:
        acronym.append(word[0])
    return ''.join(acronym)

print(makeacronym("Laugh Out Loud"))
print(makeacronym("Read the... fine manual"))
print(makeacronym("In my humble opinion"))
print(makeacronym("In my not so humble opinion"))