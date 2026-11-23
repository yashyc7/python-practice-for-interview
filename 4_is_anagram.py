def is_anagram(a, b):
    # two words are anagram of each other if they contain equal number of characters in them
    # first method is if we sort them
    a = sorted(a)
    b = sorted(b)
    return a == b


def is_anagram_2(a, b):
    ## counting occurence of each characters

    dict_a = {}
    dict_b = {}

    for i in range(len(a)):
        dict_a[a[i]] = dict_a.get(a[i], 0) + 1

    for i in range(len(b)):
        dict_b[b[i]] = dict_b.get(b[i], 0) + 1

    print(dict_a)
    print(dict_b)
    if dict_a == dict_b:
        return True


print(is_anagram_2("yash", "nitin"))
