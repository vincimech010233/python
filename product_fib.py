"""
Los números de Fibonacci son los números en la siguiente secuencia entera (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

como

F(n) = F(n-1) + F(n-2) con F(0) = 0 y F(1) = 1.

Dado un número, digamos prod (para producto), buscamos dos números de Fibonacci F(n) y F(n+1) verificando

F(n) * F(n+1) = prod.

Su función productFib toma un número entero (prod) y devuelve una matriz:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
dependiendo del idioma si F(n) * F(n+1) = prod.

Si no encuentra dos F(n) consecutivas verificando, F(n) * F(n+1) = prodregresará

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) siendo el más pequeño como F(n) * F(n+1) > prod.

Algunos ejemplos de devolución:
(depende del idioma)

productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false), 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true], 
productFib(800) # should return [34, 55, false], 
-----
productFib(714) # should return {21, 34, 1}, 
productFib(800) # should return {34, 55, 0},        
-----
productFib(714) # should return {21, 34, true}, 
productFib(800) # should return {34, 55, false}, 
Nota:
Puede ver ejemplos para su idioma en "Pruebas de muestra".

def productFib(prod):
    # your code
    return 
"""

def productFib(prod):
    a, b = 0, 1  # Inicializamos dos números de Fibonacci consecutivos: a = 0 y b = 1
    
    while a * b < prod:  # Mientras el producto de a y b sea menor que el valor dado prod
        a, b = b, a + b  # Generamos el siguiente número de Fibonacci sumando a y b
        
    return [a, b, a * b == prod]  # Devolvemos una lista con a, b y un booleano que indica si a * b es igual a prod

# Caso de prueba
print(productFib(4895))  # [55, 89, True] 55 y 89 tienen un producto igual a 4895.

