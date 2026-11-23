from collections import Counter


def find_duplicates(items):
    counts = Counter(items)
    return [x for x, c in counts.items() if c > 1]


print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
