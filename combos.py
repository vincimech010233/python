"""
Jon and Joe have received equal marks in the school examination. But, they won't reconcile in peace when equated with each other. To prove his might, Jon challenges Joe to write a program to find all possible number combos that sum to a given number. While unsure whether he would be able to accomplish this feat or not, Joe accpets the challenge. Being Joe's friend, your task is to help him out.

Task
Create a function combos, that accepts a single positive integer num (30 > num > 0) and returns an array of arrays of positive integers that sum to num.

Notes
Sub-arrays may or may not have their elements sorted.
The order of sub-arrays inside the main array does not matter.
For an optimal solution, the following operation should complete within 6000ms.
"""

def combos(num):
    if num <= 0:
        return []

    # Inicializar una lista de listas para almacenar las combinaciones
    combinations = [[] for _ in range(num + 1)]
    combinations[0] = [[]]

    # Generar combinaciones iterativamente
    for i in range(1, num + 1):
        for j in range(i, num + 1):
            for combo in combinations[j - i]:
                combinations[j].append(combo + [i])

    return combinations[num]

# Ejemplos de uso
print(combos(3))
print(combos(4))
print(combos(5))
print(combos(2))
print(combos(1))