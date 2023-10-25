"""
Un corredor que corre con velocidad base s con duración t cubrirá una distancia d: d = s * t
Sin embargo, este corredor puede correr durante una unidad de tiempo con el doble de velocidad s * 2
Después de correr, la velocidad base s se reducirá permanentemente en 1, y durante la siguiente unidad de tiempo el corredor entrará en recuperación fase y no puede correr de nuevo.

Su tarea, dada la velocidad base s y el tiempo t, es encontrar la distancia máxima posible d.

Aporte:
1 <= s < 1000
1 <= t < 1000

Ejemplo:
Dado s = 2 y t = 4.
Podríamos programar cuándo el corredor debería correr para poder obtener estas posibles secuencias:

Sec.: RRRR
=> s + s + s + s
=> 2 + 2 + 2 + 2 = 8
Sec.: RRRS
=> s + s + s + s*2
=> 2 + 2 + 2 + 2*2 = 10
Sec.: RRSR
=> s + s + s*2 + (s-1)
=> 2 + 2 + 2*2 + (2-1) = 9
Sec.: RSRR
=> s + s*2 + (s-1) + (s-1)
=> 2 + 2*2 + (2-1) + (2-1) = 8
Sec.: RSRS
=> s + s*2 + (s-1) + (s-1)*2
=> 2 + 2*2 + (2-1) + (2-1)*2 = 9
Sec.: SRRR
=> s*2 + (s-1) + (s-1) + (s-1)
=> 2*2 + (2-1) + (2-1) + (2-1) = 7
Sec.: SRRS
=> s*2 + (s-1) + (s-1) + (s-1)*2
=> 2*2 + (2-1) + (2-1) + (2-1)*2 = 8
Sec.: SRSR
=> s*2 + (s-1) + (s-1)*2 + (s-1-1)
=> 2*2 + (2-1) + (2-1)*2 + (2-1-1) = 7

Dónde:
- R: funcionamiento normal/recuperación
- S: Velocidad
Según las secuencias anteriores, la distancia máxima posible des 10.

def solution(s, t):
    pass
"""

def max_distance(s, t):
    # Caso base: Si t es 1, corremos a doble velocidad
    if t == 1:
        return s * 2
    
    # Variable para almacenar la distancia máxima
    max_distance = 0
    
    # Iterar sobre todas las posiciones posibles para correr a doble velocidad
    for i in range(t):
        # Calcular la distancia considerando correr a doble velocidad en la posición i
        distance = 0
        for j in range(t):
            if j == i:
                distance += s * 2  # Correr a doble velocidad en la posición i
            elif j < i:
                distance += s  # Correr a velocidad base antes de correr a doble velocidad
            else:  # j > i
                distance += max(s - 1, 1)  # Correr a velocidad reducida después de correr a doble velocidad
            
        # Actualizar la distancia máxima
        max_distance = max(max_distance, distance)
        
    return max_distance

# Prueba del ejemplo
print(max_distance(2, 4))  # Output: 10
