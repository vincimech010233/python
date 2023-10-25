def sort_by_name(arr):
    # Define a mapping of integers to their corresponding names
    names = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    # Define a function to convert an integer to its name
    def int_to_name(num):
        if num < 20:
            return names[num]
        elif num < 100:
            # Verifica si el número está en el rango de 20 a 99 (números de dos dígitos)
            tens = names[num // 10 * 10]  # Calcula la parte de las decenas y obtiene su nombre
            ones = names[num % 10]        # Calcula la parte de las unidades y obtiene su nombre

            # Verifica si la parte de las unidades es "zero"
            if ones == "zero":
                # Si las unidades son "zero", devuelve solo el nombre de las decenas (por ejemplo, "twenty")
                return tens
            else:
                # Si las unidades son diferentes de "zero", agrega un guión y el nombre de las unidades al nombre de las decenas (por ejemplo, "twenty-three")
                return tens + "-" + ones
        else:
            # Si el número es mayor o igual a 100, estamos tratando con números de tres dígitos
            hundreds = names[num // 100] + " hundred"  # Calcula la parte de las centenas y agrega "hundred" al nombre
            remainder = num % 100  # Calcula el residuo después de quitar las centenas

            # Verifica si el residuo es igual a cero, lo que significa que no hay decenas ni unidades
            if remainder == 0:
                # Si no hay decenas ni unidades, devuelve solo el nombre de las centenas (por ejemplo, "two hundred")
                return hundreds
            # asegurarse de que siempre devuelva una cadena
            else:
                return hundreds + " and " + int_to_name(remainder)


    # Sort the array based on the mapped names
    sorted_arr = sorted(arr, key=lambda x: int_to_name(x))
    return sorted_arr

# Example usage:
arr = [1, 2, 3, 4]
sorted_arr = sort_by_name(arr)
print(sorted_arr)  # Output: [4, 1, 3, 2]
