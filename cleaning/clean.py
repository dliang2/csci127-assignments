def read(file):
    f = open(file)
    text = f.read()
    f.close()
    return text

def clean(text):
    text = read(text)
    word_list = text.split()
    cleaned_list = []
    for word in word_list:
        if not word.isalpha():
            pass
        else:
            word = word.capitalize()
            word = word.replace("\n", " ")
            word.strip("?!.,:;-")
            cleaned_list.append(word)
    return cleaned_list

def word_count(text):
    d = {}
    word_list = clean(text)
    word_list.sort()
    for word in word_list:
        d.setdefault(word, 0)
        d[word] += 1
    return d

print(word_count("macbeth.txt"))
print("\n")
print(word_count("moby.txt"))
print("\n")
print(word_count("psalms.txt"))