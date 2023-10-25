"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints
0 <= length of input <= 100

All inputs will be strings, consisting only of characters ( and ).
Empty strings are considered balanced (and therefore valid), and will be tested.
For languages with mutable strings, the inputs should not be mutated.

Protip: If you are trying to figure out why a string of parentheses is invalid, paste the parentheses into the code editor, and let the code highlighting show you!
"""

def valid_parentheses(string):
    stack = []  # Crea una pila vacía para almacenar los paréntesis de apertura

    for char in string:  # Itera a través de cada carácter en la cadena
        try:
            if char == '(':  # Si el carácter es un paréntesis de apertura
                stack.append('(')  # Agrega el paréntesis a la pila
            elif char == ')':  # Si el carácter es un paréntesis de cierre
                if stack.pop() != '(':  # Intenta sacar un paréntesis de apertura de la pila
                    return False  # Si no coincide, la cadena es inválida
        except IndexError:  # Captura una excepción si ocurre un índice inválido en la pila (cierre sin apertura)
            return False  # La cadena es inválida
    
    return len(stack) == 0  # Si la pila está vacía al final, la cadena es válida

# Pruebas
print(valid_parentheses("()"))              # Output: True
print(valid_parentheses(")(()))"))          # Output: False
print(valid_parentheses("("))               # Output: False
print(valid_parentheses("(())((()())())"))  # Output: True
print(valid_parentheses("(()"))             # Output: False
print(valid_parentheses("())"))             # Output: False
print(valid_parentheses(")("))              # Output: False
