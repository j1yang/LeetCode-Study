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
