"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

def rgb(r, g, b):
    # your code here :)
    pass
"""

def rgb(r, g, b):
    # Asegurar que los valores estén dentro del rango de 0 a 255
    # 0 = ausencia color y 255 = maximo intensidad de color
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    
    # Convertir los valores RGB a su representación hexadecimal y devolverlos en mayúsculas
    # 02 = dos caracteres
    # X = caracter
    return f"{r:02X}{g:02X}{b:02X}"

# Pruebas
print(rgb(255, 255, 255))  # 'FFFFFF'
print(rgb(254, 253, 252))  # 'FEFDFC'
print(rgb(-141, 137, 125)) # '00897D'

