def count_word_occurrences(text, word):
    words = text.split()
    return words.count(word)
a = count_word_occurrences('Hello world, hello people', 'hello')
print(a)