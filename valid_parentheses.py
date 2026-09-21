"""Check whether a string of parentheses is balanced."""


def valid_parentheses(string: str) -> bool:
    """Return whether every opening parenthesis has a matching close."""
    stack: list[str] = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
