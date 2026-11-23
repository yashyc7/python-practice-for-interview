# for example we have string named "Python"


ex_string = "Python"


def reverse(str_input: str) -> str:
    """Returns the reversed string

    Args:
        str_input (str):string input

    Returns:
        str: returns the reverse of the input string
    """

    # method one is slicing
    return str_input[::-1]


def reverse_string_2(str_input: str) -> str:
    """Returns the reversed string

    Args:
        str_input (str):string input

    Returns:
        str: returns the reverse of the input string
    """
    # we can use the two pointer method here
    # p=0 y=1 t=2 h=3 o=4 n=5
    length = len(str_input) - 1  # 5
    res = ""
    while length >= 0:
        res = res + str_input[length]
        length = length - 1
    return res


def reverse_string_3(str_input: str) -> str:
    """Returns the reversed string

    Args:
        str_input (str):string input

    Returns:
        str: returns the reverse of the input string
    """
    start = 0
    str_input = list(str_input)
    end = len(str_input) - 1

    while start < end:
        # swap the chars
        str_input[start], str_input[end] = str_input[end], str_input[start]
        start = start + 1
        end = end - 1
    return "".join(str_input)


print(reverse("python"))
print(reverse_string_2("python"))
print(reverse_string_3("python"))
