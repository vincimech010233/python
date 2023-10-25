class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def intercambiar_pares(cabeza):
    # Si la lista está vacía o tiene solo un nodo, no hay nada que hacer
    if not cabeza or not cabeza.siguiente:
        return cabeza

    # El nuevo nodo principal será el segundo nodo actual
    nuevo_cabeza = cabeza.siguiente

    # El siguiente nodo del segundo nodo actual será la cabeza original
    cabeza.siguiente = intercambiar_pares(nuevo_cabeza.siguiente)

    # El segundo nodo se convierte en el nuevo nodo principal y apunta a la cabeza original
    nuevo_cabeza.siguiente = cabeza

    return nuevo_cabeza

# Función auxiliar para imprimir la lista enlazada
def imprimir_lista_enlazada(cabeza):
    actual = cabeza
    while actual:
        print(actual.valor, end=" --> ")
        actual = actual.siguiente
    print("Ninguno")

# Ejemplo de uso:
# Crear una lista enlazada: A --> B --> C --> D
D = Nodo('D')
C = Nodo('C', D)
B = Nodo('B', C)
A = Nodo('A', B)

print("Lista enlazada original:")
imprimir_lista_enlazada(A)

# Intercambiar pares de nodos: B --> A --> D --> C
nueva_cabeza = intercambiar_pares(A)

print("\nLista enlazada después de intercambiar pares:")
imprimir_lista_enlazada(nueva_cabeza)
