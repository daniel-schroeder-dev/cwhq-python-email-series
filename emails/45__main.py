from random import sample


def shuffle_letters(word):
    shuffled_letters = sample(word, k=len(word))
    return "".join(shuffled_letters)


print(shuffle_letters("banana"))  # aabnan
print(shuffle_letters("pizza"))  # zapiz
