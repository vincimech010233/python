import re

def is_valid_identifier(identifier):
    # Verifica si la cadena es nula o vacía
    if not identifier:
        return False
    
    # Verifica que el primer carácter sea una letra, guión bajo o signo de dólar
    if not re.match(r'^[a-zA-Z_$]', identifier[0]):
        return False
    
    # Verifica que los caracteres restantes sean letras, dígitos, guión bajo, signo de dólar o no hay espacios 
    if not re.match(r'^[a-zA-Z0-9_$]*$', identifier[1:]):
        return False
    
    return True

# Ejemplos de uso
print(is_valid_identifier("i"))      # True
print(is_valid_identifier("wo_rd"))  # True
print(is_valid_identifier("b2h"))    # True

print(is_valid_identifier("1i"))     # False
print(is_valid_identifier("wo rd"))  # False
print(is_valid_identifier("!b2h"))   # False
