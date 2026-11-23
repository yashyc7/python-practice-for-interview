def valid_parenthesis(input_string):
    # when the  most recnet needed
    # Push opening bracket in stack

    mappings = {")": "(", "]": "[", "}": "{"}
    stack = []

    # if closing bracket arrives and stack is empty then return false .
    for item in input_string:
        if item in ["(", "[", "{"]:
            stack.append(item)
        elif item in [")", "]", "}"]:
            if not stack or stack[-1] != mappings[item]:
                return False
            else:
                stack.pop()
    return True


print(valid_parenthesis("([])"))
print(valid_parenthesis("([})"))


# simple hai opening brakcet hai to stack mai push karo
# closing bracket hai to stack se match karo and then pop karlo

# if stack alr empty mean the closing bracket is coming on first which means false
# and if stack top doesn't match the closing of the item then return false
# outside the loop return the True
