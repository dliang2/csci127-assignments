import random

d = {
    "exclamations": ["'ruh-roh!'", "'zoinks!'", "'jinkies!'", "'jeepers'"],
    "adverbs": ["quickly", "amusingly", "sadly"],
    "nouns": ["dog", "hammer", "cat", "car", "frog"],
    "adjectives": ["cowardly", "questionable", "smelly"],
    "verbs": ["ate", "walked", "slept"],
    "heroes": ["Shaggy", "Velma", "Scooby-Doo", "Daphne", "Fred"]
}

paragraph1 = "<EXCLAMATION> he said <ADVERB> as he jumped into his <NOUN> and drove off with his <ADJECTIVE> wife."
paragraph2 = "Sam <VERB> the <NOUN> and then <VERB> the <NOUN> later."
paragraph3 = "<HERO> <VERB> in the <NOUN> and then <HERO> <VERB> the <NOUN> later."

def choose_random(l): # chooses random element in list
    return l[random.randrange(0, len(l))]

def stringify(l): # turns list into string
    return " ".join(l)

def madlibify(paragraph):
    word_list = paragraph.split()
    madlib_list = []
    hero = choose_random(d["heroes"]) # makes one unique hero
    for item in word_list: # check through each word
        if item == "<EXCLAMATION>":
            madlib_list.append(random.choice(d["exclamations"]))
        elif item == "<ADVERB>":
            madlib_list.append(random.choice(d["adverbs"]))
        elif item == "<NOUN>":
            madlib_list.append(random.choice(d["nouns"]))
        elif item == "<ADJECTIVE>":
            madlib_list.append(random.choice(d["adjectives"]))
        elif item == "<VERB>":
            madlib_list.append(random.choice(d["verbs"]))
        elif item == "<HERO>":
            madlib_list.append(hero)
        else:
            madlib_list.append(item)
    madlib_paragraph = stringify(madlib_list) # combine list of words back to paragraph
    return madlib_paragraph

print(madlibify(paragraph1))
print(madlibify(paragraph2))
print(madlibify(paragraph3))