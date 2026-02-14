# binary_tree.py
# Binary Search Tree implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.root = bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)

    print("Inorder traversal:")
    bst.inorder(bst.root)
