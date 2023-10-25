"""
Tap Code Translation
Tap code is a way to communicate using a series of taps and pauses for each letter. In this kata, we will use dots . for the taps and whitespaces for the pauses.

The number of taps needed for each letter matches its coordinates in the following polybius square (note the c/k position). Then you "tap" the row, a pause, then the column. Each letter is separated from others with a pause too.

   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
Input:
A lowercase string of a single word (no whitespaces or punctuation, only letters).

Output:
The encoded string as taps and pauses.

Examples
text = "dot"
  "D" = (1, 4) = ". ...."
  "O" = (3, 4) = "... ...."
  "T" = (4, 4) = ".... ...."
  
output: ". .... ... .... .... ...."


"example" -> ". ..... ..... ... . . ... .. ... ..... ... . . ....."
"more"    -> "... .. ... .... .... .. . ....."
"""

def tap_code_translation(text):
    polybius_square = {
        'A': (1, 1), 'B': (1, 2), 'C': (1, 3), 'K': (1, 3), 'D': (1, 4), 'E': (1, 5),
        'F': (2, 1), 'G': (2, 2), 'H': (2, 3), 'I': (2, 4), 'J': (2, 5),
        'L': (3, 1), 'M': (3, 2), 'N': (3, 3), 'O': (3, 4), 'P': (3, 5),
        'Q': (4, 1), 'R': (4, 2), 'S': (4, 3), 'T': (4, 4), 'U': (4, 5),
        'V': (5, 1), 'W': (5, 2), 'X': (5, 3), 'Y': (5, 4), 'Z': (5, 5)
    }
    
    result = []
    for char in text:
        row, col = polybius_square[char.upper()]
        result.append('.' * row + ' ' + '.' * col)
    
    return ' '.join(result)


print(tap_code_translation("dot"))

# Test cases with assertions
assert tap_code_translation("dot") == ". .... ... .... .... ...."
assert tap_code_translation("example") == ". ..... ..... ... . . ... .. ... ..... ... . . ....."
assert tap_code_translation("more") == "... .. ... .... .... .. . ....."

print("All test cases passed!")