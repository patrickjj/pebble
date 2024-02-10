class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.value}, {self.left}, {self.right})"

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def search(self, value):
        if self.root is None:
            return None
        else:
            return self._search(value, self.root)

    def _search(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self._search(value, node.left)
        elif value > node.value and node.right is not None:
            return self._search(value, node.right)
        else:
            return None
