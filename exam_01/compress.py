def compress_word(w):
    compressed = w[0] # keep first letter
    for letter in w[1:]: # don't touch first letter
        if letter in "aeiouAEIOU": # if vowel, do nothing
            compressed += ""
        else:
            compressed += letter # add letter
    return compressed
    
print(compress_word('halloween'))
print(compress_word('Special'))
print(compress_word('apple'))

def sentence(line):
    word_list = line.split(" ")
    compressed = ""
    for w in word_list:
        word = compress_word(w) + " "
        compressed += word
    return compressed[:-1] 

print(sentence('I like to eat apple pie.'))
print(sentence('Who is there'))