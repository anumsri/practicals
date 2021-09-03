word_count = {}
text = input("Text: ")
# "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for letter in words:
    amount = word_count.get(letter, 0)
    word_count[letter] = amount+1

words = list(word_count.keys())
words.sort()

max_length = max((len(letter) for letter in words))
for letter in words:
    print("{:{}} = {}".format(letter, max_length, word_count[letter]))


