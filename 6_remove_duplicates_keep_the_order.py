def unique(items):
    seen = set()
    result = []

    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


print(unique([3, 1, 3, 2, 1, 4]))
