def goat_latin(sentence):
    vowel = set("aeiouAEIOU")
    words = sentence.split()
    result = []

    for i, word in enumerate(words):
        if word[0] in vowel:
            new_word = word + "ma"
        else:
            new_word = word[1:] + word[0] +"ma"

        new_word = new_word + "a" * (i+1)
        result.append(new_word)
    result = " ".join(result)

    return result

print(goat_latin("I speak Goat Latin"))