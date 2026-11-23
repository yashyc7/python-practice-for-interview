def flatten_list(input_list) -> list[int]:
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # recursively
        else:
            result.append(item)
    return result


print(flatten_list([1, [2, 3], [4, [5, 6]], 7]))
