# Darren Liang and Kaitlyn Zhen

import random

exclamations = ["'ruh-roh!'", "'zoinks!'", "'jinkies!'", "'jeepers'"]
adverbs = ["quickly", "amusingly", "sadly"]
nouns = ["dog", "hammer", "cat", "car", "frog"]
adjectives = ["cowardly", "questionable", "smelly"]
verbs = ["ate", "walked", "slept"]
heroes = ["Shaggy", "Velma", "Scooby-Doo", "Daphne", "Fred"]

paragraph1 = "<EXCLAMATION> he said <ADVERB> as he jumped into his <NOUN> and drove off with his <ADJECTIVE> wife."
paragraph2 = "Sam <VERB> the <NOUN> and then <VERB> the <NOUN> later."
paragraph3 = "<HERO> <VERB> in the <NOUN> and then <HERO> <VERB> the <NOUN> later."


def choose_random(l): # chooses random element in list
    return l[random.randrange(0, len(l))]

def stringify(l): # turns list into string
    return " ".join(l)

def madlibify(paragraph):
    word_list = paragraph.split() # split the paragraph into a list
    madlib_list = [] # list of words that madlib paragraph will use
    hero = choose_random(heroes) # makes one unique hero
    for item in word_list: # check through each word
        if item == "<EXCLAMATION>":
            madlib_list.append(random.choice(exclamations))
        elif item == "<ADVERB>":
            madlib_list.append(random.choice(adverbs))
        elif item == "<NOUN>":
            madlib_list.append(random.choice(nouns))
        elif item == "<ADJECTIVE>":
            madlib_list.append(random.choice(adjectives))
        elif item == "<VERB>":
            madlib_list.append(random.choice(verbs))
        elif item == "<HERO>":
            madlib_list.append(hero)
        else:
            madlib_list.append(item)
    madlib_paragraph = stringify(madlib_list) # combine list of words back to paragraph
    return madlib_paragraph

print(madlibify(paragraph1))
print(madlibify(paragraph2))
print(madlibify(paragraph3))