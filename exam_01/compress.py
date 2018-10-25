def compress_word(w):
    compressed = w[0] # keep first letter
    for letter in w[1:]: # don't touch first letter
        if letter not in "aeiouAEIOU": # if not vowel, add letter
            compressed += letter 
    return compressed
    
print(compress_word('halloween'))
print(compress_word('Special'))
print(compress_word('apple'))

def sentence(line):
    word_list = line.split(" ")
    compressed_words = []
    for w in word_list:
        compressed_words.append(compress_word(w))
    compressed = " ".join(compressed_words)
    return compressed 

print(sentence('I like to eat apple pie.'))
print(sentence('Who is there'))