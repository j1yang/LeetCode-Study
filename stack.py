# 20
def isValid(self, s: str) -> bool:
    d = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    stack = []

    for char in s:
        # If it's an opening bracket, add it to the stack
        if char in d:
            stack.append(char)

        # If there's something in the stack
        elif stack:
            # If it's a closing bracket for the last opened bracket, remove it from the stack.
            if char == d[stack[-1]]:
                stack.pop()

            # It's not a closing bracket for the last opened bracket. Invalid string.
            else:
                return False

        # Not an opening bracket or closing bracket. Invalid string.
        else:
            return False

    # True if all characters have been checked and stack is empty.
    # False if all characters have been checked but the stack is not empty. Meaning there is an
    # unclosed bracket.
    return stack == []

# 125 Valid Palindrome


def isPalindrome(self, s: str) -> bool:
    res = str(s).lower()
    stack = []

    for i in res:
        if i.isalnum():
            stack.append(i)

    if not stack:
        return True
    else:
        for ch in stack:
            if ch == stack[-1]:
                stack.pop()
            else:
                return False
