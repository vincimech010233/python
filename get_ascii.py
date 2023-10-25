"""
Get ASCII value of a character.

For the ASCII table you can refer to http://www.asciitable.com/
"""

def get_ascii(ch : str) -> int:
    return ord(ch)


if __name__ == '__main__':
    print(get_ascii('A'))  # 65


