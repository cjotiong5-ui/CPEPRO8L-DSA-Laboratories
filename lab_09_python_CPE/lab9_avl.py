class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_right(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        self.update_height(root)

        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key) + f" (h={node.height}, b={self.get_balance(node)})")
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Test 1: Insert [10, 20, 30] — triggers LL case (left rotation)
    print("=" * 50)
    print("Test 1: Insert [10, 20, 30]")
    print("=" * 50)
    for key in [10, 20, 30]:
        root = avl.insert(root, key)
        print(f"\nAfter inserting {key}:")
        avl.print_tree(root)

    print("\nInorder:", end=" ")
    avl.inorder(root)
    print("\n")

    # Test 2: Insert [30, 20, 10] — triggers RR case (right rotation)
    print("=" * 50)
    print("Test 2: Insert [30, 20, 10]")
    print("=" * 50)
    root2 = None
    for key in [30, 20, 10]:
        root2 = avl.insert(root2, key)
        print(f"\nAfter inserting {key}:")
        avl.print_tree(root2)

    print("\nInorder:", end=" ")
    avl.inorder(root2)
    print("\n")

    # Test 3: Insert [10, 30, 20] — triggers LR case
    print("=" * 50)
    print("Test 3: Insert [10, 30, 20]")
    print("=" * 50)
    root3 = None
    for key in [10, 30, 20]:
        root3 = avl.insert(root3, key)
        print(f"\nAfter inserting {key}:")
        avl.print_tree(root3)

    print("\nInorder:", end=" ")
    avl.inorder(root3)
    print("\n")

    # Test 4: Insert [30, 10, 20] — triggers RL case
    print("=" * 50)
    print("Test 4: Insert [30, 10, 20]")
    print("=" * 50)
    root4 = None
    for key in [30, 10, 20]:
        root4 = avl.insert(root4, key)
        print(f"\nAfter inserting {key}:")
        avl.print_tree(root4)

    print("\nInorder:", end=" ")
    avl.inorder(root4)
    print("\n")
