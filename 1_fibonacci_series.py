"""
Write a python program that prints the first n numbers of the Fibonacci series .
Input: n = 10
Output [0,1,1,2,3,5,8,13,21,34]
"""

# my solution


def fibonacci(n: int) -> list[int]:
    """Returns the fibonacci series list of  values of first 'n' provided values

    Args:
        n (int): Takes integer value

    Returns:
        List[int]: List of the integer values that represent the fibonacci series for values n
    """
    a, b = 0, 1

    result = []

    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


## or second this can be this


def fibonacci_2(n: int) -> list[int]:
    """Another method for fibonacci here

    Args:
        n (int): taking n input

    Returns:
        list[int]: returning fibonacci series
    """

    if n < 2:
        return n
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)
