class BinaryTree(object):
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

        def __str__(self):
            return "(Node: " + str(self.data) + ")"

    def __init__(self, root = None):
        self.root = root

    # Wrapper for the recursive function _add
    def add(self, val):
        if self.root == None:
            self.root = BinaryTree.Node(val)
        else:
            self._add(self.root, val)

    # Insert a val in the tree starting at a certain node
    # Traverse the tree until we find an empty spot,
    # going right when the val is greater than the node's
    # val and left in the other case
    def _add(self, node, val):
        if val < node.data:
            if node.left == None:
                node.left = BinaryTree.Node(val)
            else:
                return self._add(node.left, val)
        else:
            if node.right == None:
                node.right = BinaryTree.Node(val)
            else:
                return self._add(node.right, val)

    # Wrapper for the recursive function _find
    def find(self, val):
        if self.root == None:
            return None
        else:
            return self._find(self.root, val)

    # Find a val in the tree starting at a certain node
    # going right when the val is greater than the node's
    # val and left in the other case
    def _find(self, node, val):
        if val == node.data:
            return node
        elif val < node.data and node.left != None:
            self._find(node.left, val)
        elif val > node.data and node.right != None:
            self.find(node.right, val)

    def visit(self, node):
        print node

    # Preorder tree traversal starts by visiting the root of
    # the tree, then visits every left children and then visits
    # all the right children
    def preOrder(self, node):
        if node == None:
            return
        self.visit(node)
        self.preOrder(node.left)
        self.preOrder(node.right)

    # Inorder tree traversal starts by visiting every left child of
    # the tree, then visits the root and then visits
    # all the right children
    def inOrder(self, node):
        if node == None:
            return
        self.inOrder(node.left)
        self.visit(node)
        self.inOrder(node.right)

    # Postorder tree traversal starts by visiting every left child of
    # the tree, then visits every right child and finishes with
    # the root.
    def postOrder(self, node):
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        self.visit(node)

tree = BinaryTree()
tree.add(20)
tree.add(15)
tree.add(25)
tree.add(10)
tree.add(17)
tree.add(18)
tree.add(22)
tree.add(27)
tree.add(29)
#
#        20
#     /      \
#    15       25
#    / \    /    \
# 10    17  22    27
#        \        \
#        18       29
# 20 15 10 17 18 25 22 27 29
# 10 15 17 18 20 22 25 27 29
# 10 18 15 22 29 27 25 20
print "preorder"

tree.preOrder(tree.root)

print "==============="

print "inorder"

tree.inOrder(tree.root)

print "==============="

print "postorder"

tree.postOrder(tree.root)

print "==============="
