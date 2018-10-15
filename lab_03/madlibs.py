# Darren Liang and Kaitlyn Zhen

import random

exclamations = ["ouch!", "zoinks!", "jinkies!"]
adverbs = ["quickly", "amazingly", "sadly"]
nouns = ["dog", "hammer", "cat", "car", "frog"]
adjectives = ["tiny", "questionable", "smelly"]
verbs = ["ate", "walked", "slept"]
heroes = ["Flash", "Robin", "Thor"]

paragraph1 = "<EXCLAMATION> he said <ADVERB> as he jumped into his <NOUN> and drove off with his <ADJECTIVE> wife."
paragraph2 = "Sam <VERB> the <NOUN> and then <VERB> the <NOUN> later"
paragraph3 = "<HERO> <VERB> in the <NOUN> and then <HERO> <VERB> <NOUN> later."


def choose_random(l):
    return l[random.randrange(0, len(l))]

def stringify(l):
    return " ".join(l)

def madlibify(paragraph):
    word_list = paragraph.split()
    madlib_list = []
    hero = choose_random(heroes)
    for item in word_list:
        if item == "<EXCLAMATION>":
            madlib_list.append(choose_random(exclamations))
        elif item == "<ADVERB>":
            madlib_list.append(choose_random(adverbs))
        elif item == "<NOUN>":
            madlib_list.append(choose_random(nouns))
        elif item == "<ADJECTIVE>":
            madlib_list.append(choose_random(adjectives))
        elif item == "<VERB>":
            madlib_list.append(choose_random(verbs))
        elif item == "<HERO>":
            madlib_list.append(hero)
        else:
            madlib_list.append(item)
    madlib_paragraph = stringify(madlib_list)
    return madlib_paragraph

print(madlibify(paragraph1))
print(madlibify(paragraph2))
print(madlibify(paragraph3))
        
            
            
    
    