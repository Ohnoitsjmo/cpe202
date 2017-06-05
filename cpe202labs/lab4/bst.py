# Justin Mo

# BinarySearchTree is a wrapper class BinarySearch Tree
class BinarySearchTree:
    def __init__(self, comes_before):
       self.comes_before = comes_before
       self.root = None
       self.size = 0

    def __repr__(self):
        return "Node: {!r}, Size: {!r}".format(self.root, self.size)

    def __eq__(self, other):
        return type(other) == BinarySearchTree and self.root == other.root and self.size == other.size

# Given a BST, returns an iterator (using yield) of the elements in prefix order for a given node where the node is visiter before its children and left child is visited before the right child
def prefix_iterator(bst):
    if type(bst) == BinarySearchTree:
        yield from prefix_iterator(bst.root)
    if bst is not None:
        yield bst.value
        yield from prefix_iterator(bst.left)
        yield from prefix_iterator(bst.right)

# Given a BST, returns an iterator (using yield) for a given node that is visited after the left child but before the right
def infix_iterator(bst):
    if type(bst) == BinarySearchTree:
        yield from infix_iterator(bst.root)  
    if bst is not None:
        yield from infix_iterator(bst.left)
        yield bst.value
        yield from infix_iterator(bst.right)


# Given a BST, returns an iterator (using yield) of the elements in postfix order where the node is visited after its children
def postfix_iterator(bst):
    if type(bst) == BinarySearchTree:
        yield from postfix_iterator(bst.root)
    if bst is not None:
        yield from postfix_iterator(bst.left)
        yield from postfix_iterator(bst.right)
        yield bst.value



# Node is one of:
# -- None or
# -- Node(value, left, right)
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node(Parent: {!r}, Left: {!r}, Right: {!r})".format(self.value, self.left, self.right)
    
    def __eq__(self, other):
        return type(other) == Node and self.value == other.value and self.left == other.left and self.right == other.right

# value value -> bool
# Takes in two nodes and compares their values and returns a bool based on the value
def comes_before(a, b):
    return (a <= b)

# BST -> bool
# Takes in a BST and returns a bool based on whether it's empty or not.
def is_empty(bst):
    if bst == None:
        return True
    elif bst.root == None:
        return True
    return False

# BST value -> BST
# Takes in a BST and adds the value to the appropriate node in the tree
def insert(bst, val):
    if bst == None:
        return Node(val, None, None)
    elif type(bst) == BinarySearchTree:
        bst.size += 1
        return insert(bst.root, val)
    else:
        if comes_before(val, bst.value) ==  True:
            return Node(bst.value, insert(bst.left, val), bst.right)
        if comes_before(val, bst.value) == False:
            return Node(bst.value, bst.left, insert(bst.right, val)) 

# BST value -> bool
# Takes in a BST and a value and returns a bool based on whether the value is in the BST
def lookup(bst, val):
    if type(bst) == BinarySearchTree:
        return lookup(bst.root, val)
    elif bst == None:
        return False
    else:
        if val == bst.value:
            return True
        elif comes_before(val, bst.value) == True:
            return lookup(bst.left, val)
        else:
            return lookup(bst.right, val)

# BST value -> BST
# Takes in a BST and a value and removes the value from the tree. If there are duplicates, only one of the duplicates are removed.
def delete(bst, val):
    if type(bst) == BinarySearchTree:
        if lookup(bst, val) == False:
            return bst.root
        elif val == bst.root.value and bst.size == 1:
            bst.size = 0
            bst = None
            return bst
        bst.size -= 1
        return delete(bst.root, val)
    elif val == bst.value:
        if bst.left == None and bst.right == None:
            bst = None
            return bst
        elif (bst.left == None and bst.right != None):
            bst = bst.right
            return bst
        elif (bst.right == None and bst.left != None):
            bst = bst.left
            return bst
        else:
            minimum = min_helper(bst.right)
            bst = delete(bst, minimum)
            bst.value = minimum
            return bst
    else:
        if comes_before(val, bst.value) == True:
            return Node(bst.value, delete(bst.left, val), bst.right)
        else:
            return Node(bst.value, bst.left, delete(bst.right, val))

# BST -> value
# Takes in a BST and return the smallest value
def min_helper(bst):
    if bst.left != None:
        return min_helper(bst.left)
    return bst.value


