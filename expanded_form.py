"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    pass
"""

# expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(num):
    if num == 0:
        return '0'  # Si el número es cero, la forma es simplemente '0'

    num_str = str(num)  # Convertir el número en una cadena para trabajar con los dígitos
    result = []  # Lista para almacenar los términos 

    for i, digit in enumerate(num_str):
        if digit != '0':  # Solo considera los dígitos diferentes de cero
            # Crear un término multiplicando el dígito por la potencia de 10 correspondiente a su posición
            term = digit + '0' * (len(num_str) - i - 1)
            result.append(term)  # Agregar el término a la lista de resultados

    return ' + '.join(result)  # Unir los términos con ' + ' para obtener la forma expandida
# Pruebas
def test_expanded_form():
    assert expanded_form(12) == '10 + 2'
    assert expanded_form(42) == '40 + 2'
    assert expanded_form(70304) == '70000 + 300 + 4'
    assert expanded_form(5000) == '5000'
    assert expanded_form(0) == '0'

    print("Todas las pruebas pasaron con éxito!")
    # Prueba no pasa -> AssertionError

test_expanded_form()


def test_expanded_form():
    assert expanded_form(12) == '10 + 2'
    assert expanded_form(42) == '40 + 2'
    assert expanded_form(70304) == '70000 + 300 + 4'
    assert expanded_form(5000) == '5000'
    assert expanded_form(0) == '0'

test_expanded_form()

