import math

def numero_de_digitos(n):
    # Caso especial cuando n es 0, ya que el logaritmo de 0 no está definido
    if n == 0:
        return 1  # 0 tiene 1 dígito
    
    # Para n > 0:
    # La función logaritmo base 10 (math.log10) calcula la potencia a la que 10 debe ser elevado para obtener n.
    # Por ejemplo, log10(100) es 2, porque 10^2 = 100.
    # El logaritmo base 10 de un número incrementa en 1 cada vez que el número n se multiplica por 10.
    # Por ejemplo, log10(1000) = 3, log10(10000) = 4, y así sucesivamente.
    # Por lo tanto, el valor entero de log10(n) + 1 nos dará el número de dígitos en n.
    # La función math.floor redondea hacia abajo al entero más cercano, asegurando que obtenemos el número correcto de dígitos.
    return math.floor(math.log10(n)) + 1


print(numero_de_digitos(34))
print(numero_de_digitos(345))