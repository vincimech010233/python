import dis 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(inorder, postorder):
    inorder_pos_map = {num: idx for idx, num in enumerate(inorder)}
    post_idx = [len(postorder) - 1]
    
    def construct(in_left, in_right):
        if in_left > in_right:
            return None
        root_value = postorder[post_idx[0]]
        root = TreeNode(root_value)
        root_idx = inorder_pos_map[root_value]
        post_idx[0] -= 1
        root.right = construct(root_idx + 1, in_right)
        root.left = construct(in_left, root_idx - 1)
        return root
    
    # Desensamblar la función interna construct
    print("Bytecode para 'construct'")
    dis.dis(construct)
    
    return construct(0, len(inorder) - 1)

# Desensamblar la función build_tree
print("Bytecode para 'build_tree'")
dis.dis(build_tree)


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

# Test de la función
tree1 = build_tree([4, 2, 1, 5, 3, 6], [4, 2, 5, 6, 3, 1])
print("Tree 1")
print_tree(tree1)

tree2 = build_tree([4, 2, 1, 5, 3, 6], [4, 2, 5, 1, 6, 3])
print("\nTree 2")
print_tree(tree2)
