# ჩვენს დაწერილ BST-ში დაამატეთ მეთოდი რომელიც დაბეჭდავს leaf node-ებს

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
class BST:
    def __init__(self):
        self.root = None
 
    def _insert(self, node, data):
        if node is None:
            return Node(data)
 
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
 
        return node
 
    def insert(self, data):
        self.root = self._insert(self.root, data)
 
    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.data, "-> Root")
            else:
                print(node.data, "-> ", parent.data)
 
            self._print_parents(node.left, node)
            self._print_parents(node.right, node)
 
    def print_parents(self):
        print("Parents are: ")
        self._print_parents(self.root, None)

    
    def _print_leaf_nodes(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.data, end=", ")
            
            self._print_leaf_nodes(node.left)
            self._print_leaf_nodes(node.right)

    def print_leaf_nodes(self):
        print("\nLeaf nodes are: ")
        self._print_leaf_nodes(self.root)


tree = BST()

my_list = [50, 30, 70, 20, 40, 60, 80]
for i in my_list:
    tree.insert(i)

tree.print_leaf_nodes()

