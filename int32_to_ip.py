"""
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

Examples
2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"
"""
def int32_to_ip(int32):
    if not isinstance(int32, int) or not 0 <= int32 <= 4294967295:
        return "Valor inválido"
    
    # Paso 1: Convertir el número entero de 32 bits a su representación binaria con ceros iniciales
    binary_str = format(int32, '032b')
    
    # Paso 2: Dividir la cadena binaria en 4 octetos de 8 bits cada uno
    octetos = [binary_str[i:i+8] for i in range(0, 32, 8)]
    
    # Paso 3: Convertir cada octeto de binario a decimal y unirlos con puntos
    direccion_ip = '.'.join(str(int(octeto, 2)) for octeto in octetos)
    
    return direccion_ip

# Ejemplos
print(int32_to_ip(2149583361))  # Debería imprimir "128.32.10.1"
print(int32_to_ip(32))           # Debería imprimir "0.0.0.32"
print(int32_to_ip(0))            # Debería imprimir "0.0.0.0"


