class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node is None:
        return []

    result = []
    queue = [node]

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result

# Ejemplos de uso
# Crear los nodos del ejemplo 1
node_1 = Node(None, None, 1)
node_3 = Node(None, None, 3)
node_4 = Node(None, None, 4)
node_5 = Node(None, None, 5)
node_8 = Node(node_1, node_3, 8)
node_9 = Node(node_4, node_5, 9)
node_2 = Node(node_8, node_9, 2)

# Obtener la lista ordenada por niveles
result1 = tree_by_levels(node_2)
print(result1)  # Debería imprimir [2, 8, 9, 1, 3, 4, 5]

# Crear los nodos del ejemplo 2
node_3 = Node(None, None, 3)
node_7 = Node(None, None, 7)
node_5 = Node(None, node_7, 5)
node_8 = Node(node_3, None, 8)
node_4 = Node(None, node_5, 4)
node_1 = Node(node_8, node_4, 1)

# Obtener la lista ordenada por niveles
result2 = tree_by_levels(node_1)
print(result2)  # Debería imprimir [1, 8, 4, 3, 5, 7]


