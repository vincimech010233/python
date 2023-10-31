def evens_and_odds(n):
    if n % 2 == 0:  # Check if the number is even
        return bin(n)[2:]  # Convert to binary and remove the "0b" prefix
    else:  # The number is odd
        return hex(n)[2:].lower()  # Convert to hexadecimal and remove the "0x" prefix, also make sure it is in lower case

print(evens_and_odds(2))  # Output should be "10" (binary representation of 2)
print(evens_and_odds(13))  # Output should be "d" (hexadecimal representation of 13)
