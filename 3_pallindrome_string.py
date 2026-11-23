"""Check if a string reads the same forwards and backwards. Ignore spaces, punctuation and upper/lower case.

Input: "A man, a plan, a canal: Panama" → Output: True
Input: "hello" → Output: False
"""


def is_pallindrome(s):
    # we have to first refine the string as i can see it also can have the special characters so lets we can remove it first
    final_refined_string = ""
    for ch in s:
        if ch.isalnum():  # keep it
            ch = ch.lower()
            final_refined_string = final_refined_string + ch
    print(final_refined_string)
    return final_refined_string == final_refined_string[::-1]


print(is_pallindrome("A man, a plan, a canal: Panama"))
