"""
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
"""

def to_weird_case(string):
    # Split the string into words
    # Create a new list of words
    # For each word in the list:
        # Create a new list of letters
        # For each index, letter in the list of letters:
            # If the index is even:
                # Convert the letter to uppercase
            # Otherwise:
                # Convert the letter to lowercase
        # Join the list of letters together
        # Add the new word to the new list of words
    # Join the list of words together
    # Return the new string
    words = string.split(" ") # ["String", "with", "a", "\"quote\"", "inside"]
    new_words = [] 
    for word in words: 
        letters = list(word) # ["S", "t", "r", "i", "n", "g"]
        for index, letter in enumerate(letters): # [(0, "S"), (1, "t"), (2, "r"), (3, "i"), (4, "n"), (5, "g")]
            if index % 2 == 0: # 0, 2, 4
                letters[index] = letter.upper() 
            else:
                letters[index] = letter.lower()
        new_word = "".join(letters) # "StRiNg"
        new_words.append(new_word) # ["StRiNg", "wItH", "A", "\"qUoTe\"", "iNsIdE"]
    return " ".join(new_words)


print("String with a \"quote\" inside")
print(to_weird_case("String with a \"quote\" inside"))