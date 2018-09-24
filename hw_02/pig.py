"Darren Liang, Darren Zou"

vowels = ["a", "e", "i", "o", "u"]
def piglatinify(word):
        if word[0].lower() in vowels:
            return word + "ay"
        else:
            return word[1:] + word[0] + "ay"

print(piglatinify("Cake"))
print(piglatinify("Apple"))
