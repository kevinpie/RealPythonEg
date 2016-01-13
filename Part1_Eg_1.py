def add_underscores(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = new_word+ word[i]+"_"
        print new_word
    return new_word

print add_underscores("hello")