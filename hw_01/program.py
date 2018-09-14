def capitalize(name):
    first = name.split(" ")[0]
    last = name.split(" ")[1]
    return first.capitalize() + " " +last.capitalize()
print(capitalize("darren liang"))

def init(name):
    first_initial = name[0]
    last = name.split(" ")[1]
    return first_initial.capitalize() + ". " + last.capitalize()
print(init("darren liang"))

def part_pig_latin(name):
    return name[1:] + name[0] + "ay"
print(part_pig_latin("hello"))

def make_out_word(out, word):
    return out[:2] + word + out[2:]
print(make_out_word("****", "bold"))

def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"
print(make_tags("u", "underline"))

