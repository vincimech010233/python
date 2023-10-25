"""
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
"""


"""
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
"""

def rot13(text):
    decoded = ""
    for char in text:
        if 'a' <= char <= 'z':
            # Applies ROT13 encryption to each char character, shifting 13 positions forward
            decoded += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            decoded += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            decoded += char
    return decoded

# Test examples
encoded_joke = "Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."
decoded_joke = rot13(encoded_joke)
print(decoded_joke)

# Assert 
assert rot13("EBG13 rknzcyr.") == "ROT13 example."
print("All tests passed.")