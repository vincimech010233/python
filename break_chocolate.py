"""
Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.
"""

def break_chocolate(n, m):
    assert isinstance(n, int) and isinstance(m, int), "Las dimensiones deben ser números enteros."
    assert n >= 0 and m >= 0, "Las dimensiones deben ser números enteros no negativos."
    
    if n == 0 or m == 0:
        return 0
    return (n * m) - 1 # -1 porque no se puede dividir 1 


assert break_chocolate(2, 1) == 1
assert break_chocolate(3, 1) == 2
assert break_chocolate(4, 4) == 15
assert break_chocolate(1, 1) == 0

print("Todas las pruebas pasaron correctamente.")
