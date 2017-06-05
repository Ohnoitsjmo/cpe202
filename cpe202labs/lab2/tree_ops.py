import unittest
# Justin Mo
# * Section 2 (Trees)

# * dd: NumTree Data Definition
# A NumTree is one of
# -- "mt" or
# -- TreeNode(value, left, right)
class TreeNode:
   def __init__(self, value, left, right):
      self.value = value
      self.left = left
      self.right = right

   def __repr__(self):
      return "TreeNode({!r},{!r},{!r})".format(self.value, self.left, self.right)

   def __eq__(self, other):
      return type(other) == TreeNode and self.value == other.value and self.left == other.left and self.right == other.right

# * 1:
# NumTree -> int
# Takes in tree and returns the number of elements in the tree  
def size(tree):
   if tree == "mt":
      return 0
   return 1 + size(tree.left) + size(tree.right)

# * 2:
# NumTree -> int
# Takes in tree and returns the number of leaves
def num_leaves(tree):
   if tree == "mt":
      return 0
   if tree.left == "mt" and tree.right == "mt":
      return 1
   return num_leaves(tree.left) + num_leaves(tree.right)
   
# * 3:
# NumTree -> int
# Takes in tree and returns the sum of the elements in the tree
def sum(tree):
   if tree == "mt":
      return 0
   else:
      return tree.value + sum(tree.left) + sum(tree.right)

# * 4:
# NumTree -> int
# Takes in tree and returns the height of the tree
def height(tree):
   if tree == "mt":
      return 0
   else:
      return max(height(tree.right), height(tree.left)) + 1

# * 5:
# NumTree -> bool
# Takes in a tree and returns a bool depending on whether a child node is 3 times the value of a parent node in the tree
def has_triple(tree):
   if tree == "mt":
      return False
   if tree.right != "mt":
      if tree.right.value == 3*tree.value:
         return True
   if tree.left != "mt":
      if tree.left.value == 3*tree.value:
         return True
   return has_triple(tree.left) or has_triple(tree.right)
 
# * 6:
# NumTree -> NumTree
# Takes in a tree and decreases every value in the tree by one
def sub_one_map(tree):
   if tree == "mt":
      return "mt"
   else:
      return TreeNode(tree.value - 1, sub_one_map(tree.left), sub_one_map(tree.right))

# * Tests : the test case class for the tree functions

class Test(unittest.TestCase):
   def test_repr(self):
      self.assertEqual(repr(TreeNode(4, "mt", "mt")), str(TreeNode(4, "mt", "mt")))
   def test_size(self):
      self.assertEqual(size(TreeNode(4, TreeNode(9, TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")), TreeNode(42, "mt", TreeNode(7, "mt", "mt")))), 7)
      self.assertEqual(size("mt"), 0)
      self.assertEqual(size(TreeNode(4, "mt", "mt")), 1)
   def test_sum(self):
      self.assertEqual(sum(TreeNode(4, TreeNode(9, TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")), TreeNode(42, "mt", TreeNode(7, "mt", "mt")))), 186)
      self.assertEqual(sum("mt"), 0)
      self.assertEqual(sum(TreeNode(5, "mt", "mt")), 5)
   def test_num_leaves(self):
      self.assertEqual(num_leaves("mt"), 0)
      self.assertEqual(num_leaves(TreeNode(4, TreeNode(9, TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")), TreeNode(42, "mt", TreeNode(7, "mt", "mt")))), 3)
   def test_height(self):   
      self.assertEqual(height("mt"), 0)
      self.assertEqual(height(TreeNode(6, "mt", "mt")), 1)
      self.assertEqual(height(TreeNode(4, TreeNode(9, TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")), TreeNode(42, "mt", TreeNode(7, "mt", "mt")))), 4)
   def test_has_triple(self):
      self.assertEqual(has_triple("mt"), False)
      self.assertEqual(has_triple(TreeNode(5, "mt", "mt")), False)
      self.assertEqual(has_triple(TreeNode(4, TreeNode(12, TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")), TreeNode(42, "mt", TreeNode(7, "mt", "mt")))), True)
      self.assertEqual(has_triple(TreeNode(4, TreeNode(13, TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")), TreeNode(42, "mt", TreeNode(7, "mt", "mt")))), False)
      self.assertEqual(has_triple(TreeNode(4, TreeNode(11, TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")), TreeNode(3, "mt", TreeNode(9, "mt", "mt")))), True)
   def test_sub_one_map(self):
      self.assertEqual(sub_one_map("mt"), "mt")
      self.assertEqual(sub_one_map(TreeNode(5, "mt", "mt")), TreeNode(4, "mt", "mt"))
      self.assertEqual(sub_one_map(TreeNode(4, TreeNode(12, TreeNode(19, "mt", "mt"), TreeNode(2, TreeNode(103, "mt", "mt"), "mt")), TreeNode(42, "mt", TreeNode(7, "mt", "mt")))),TreeNode(3, TreeNode(11, TreeNode(18, "mt", "mt"), TreeNode(1, TreeNode(102, "mt", "mt"), "mt")), TreeNode(41, "mt", TreeNode(6, "mt", "mt"))))
if __name__ == '__main__':
   unittest.main()
