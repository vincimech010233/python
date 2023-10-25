class Primes:
    @staticmethod
    def stream():
        primes = []  # Lista para almacenar los primos encontrados
        candidate = 2  # El primer número primo
        while True:  # Bucle infinito
            is_prime = True  # Asumir que candidate es primo hasta que se demuestre lo contrario
            for prime in primes:
                if candidate % prime == 0:  # Si candidate es divisible por algún primo, no es primo
                    is_prime = False
                    break
                if prime * prime > candidate:  # No es necesario verificar primos mayores que la raíz cuadrada de candidate
                    break
            if is_prime:  # Si candidate es primo
                yield candidate  # Genera el número primo
                primes.append(candidate)  # Añade el primo a la lista
            candidate += 1  # Prueba el siguiente número

# Ejemplo de uso:
prime_generator = Primes.stream()
for _ in range(10):
    print(next(prime_generator))  # Imprime los primeros 10 números primos
