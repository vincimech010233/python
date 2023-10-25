"""
To give credit where credit is due: This problem was taken from the ACMICPC-Northwest Regional Programming Contest. Thank you problem writers.

You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system, and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]
He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear. Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s. If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune exists.
"""

def solve_runes(expression):
    # Iterar a través de los dígitos del 0 al 9
    for i in range(10):
        # Verificar si el dígito actual no está presente en la expresión y si no comienza con un "-"
        if str(i) not in expression and (expression[0] != '-' or i != 0):
            # Reemplazar el signo de interrogación con el dígito actual
            exp = expression.replace('?', str(i)) 
            # Dividir la expresión en los lados izquierdo y derecho de la ecuación
            izquierda, derecha = exp.split('=')
            # Evaluar los lados izquierdo y derecho de la ecuación y comparar si son iguales
            if eval(izquierda) == eval(derecha):
                return i
    # Si no se encuentra ningún dígito que cumpla la ecuación, retornar -1
    return -1

# Prueba de ejemplo
expresion = "1+1=?"
# expresion = "10+2=?"
resultado_esperado = 2
resultado_obtenido = solve_runes(expresion)
assert resultado_obtenido == resultado_esperado, f"Esperado: {resultado_esperado}, Obtenido: {resultado_obtenido}"
print("Prueba pasada!")
print("resultado_obtenido: ", resultado_obtenido)


