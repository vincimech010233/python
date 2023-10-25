def square_digits(num):
    # Convert the number to a string to iterate through its digits
    num_str = str(num)
    
    # Initialize an empty string to store the result
    result_str = ""
    
    # Iterate through the digits of the number
    for digit_str in num_str:
        # Convert the digit back to an integer, square it, and convert it back to a string
        squared_digit_str = str(int(digit_str) ** 2)
        
        # Append the squared digit to the result string
        result_str += squared_digit_str
    
    # Convert the result string back to an integer and return it
    return int(result_str)

resultado = square_digits(9119)
print(resultado)  # Salida: 811181

resultado = square_digits(765)
print(resultado)  # Salida: 493625
