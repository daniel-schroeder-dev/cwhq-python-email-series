from collections import Counter


def count_num_letters(sentence):
    count_letters = Counter(sentence.lower())

    print(f"Count of different letters in '{sentence}':")
    for letter, count in count_letters.items():
        if count > 0 and letter.isalnum():
            print(letter, count)


count_num_letters("Hey, what's up?")
