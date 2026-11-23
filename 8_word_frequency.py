"""Given a text, count how many times each word appears.

Input: "the cat and the dog and the bird"
Output: {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}"""


def word_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


print(word_count("the cat and the dog and the bird"))
