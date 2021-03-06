def read(file):
    f = open(file)
    text = f.read()
    f.close()
    return text

def clean(text):
    text = read(text)
    for p in "?!.:,;—\"'“”":
        text = text.replace(p, " ")
    word_list = text.split()
    word_list = [word.capitalize() for word in word_list]
    for word in word_list:
        if not word.replace("-", "").isalpha():
             word_list.remove(word) 
    return word_list

'''
def word_count(text):
    d = {}
    word_list = clean(text)
    word_list.sort()
    for word in word_list:
        d.setdefault(word, 0)
        d[word] += 1
    return d

def most_common(text):
    d = word_count(text)
    common_words = {}
    max_count = max(d.values())
    for k, v in d.items():
        if v == max_count:
            common_words[k] = v
    return common_words

def least_common(text):
    d = word_count(text)
    common_words = {}
    min_count = min(d.values())
    for k, v in d.items():
        if v == min_count:
            common_words[k] = v
    return common_words
'''

def word_pairs(text):
    word_list = clean(text)
    d = {}
    for word in word_list:
        d[word] = []
    counter = 0
    while counter < len(word_list) - 1:
        word = word_list[counter]
        if word_list[counter + 1] not in d[word]:
            d[word].append(word_list[counter + 1])
            #if next not in d[word]:
            #d[word].append(next)
        counter += 1
        
    return d

#print(clean("macbeth.txt"))
#print(clean("moby-small.txt"))
#print(clean("psalms.txt"))

#print("\n")

#print(word_pairs("macbeth.txt"))
print(word_pairs("moby-small.txt"))
#print(word_pairs("psalms.txt"))

#print("\n")

#print(word_count("macbeth.txt"))
#print(most_common("macbeth.txt"))
#print(least_common("macbeth.txt"))

#print("\n")

#print(word_count("moby-small.txt"))
#print(most_common("moby-small.txt"))
#print(least_common("moby-small.txt"))

#print("\n")

#print(word_count("psalms.txt"))
#print(most_common("psalms.txt"))
#print(least_common("psalms.txt"))
