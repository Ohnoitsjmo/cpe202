import unittest
# * Section 1 (Lists)

# * dd: NumList Data Definition
# A NumList is one of 
# -- "mt" or
# -- Pair(value, rest)
class Pair:
   def __init__(self, value, rest):
      self.value = value # an int
      self.rest = rest # a NumList
   
   def __repr__(self):
      return "Pair({!r},{!r})".format(self.value, self.rest)

   def __eq__(self, other):
      return type(other) == Pair and self.value == other.value and self.rest == other.rest
     
# * 1:
# NumList -> int
# Takes in a numlist and returns the length of the list
def length(numlist):
   if numlist == "mt":
      return 0
   else:
      return 1 + length(numlist.rest)

# * 2:
# NumList -> int
# Takes in a numlist and returns the sum of the list
def sum(numlist):
   if numlist == "mt":
      return 0
   return numlist.value + sum(numlist.rest)

# * 3:
# NumList number -> int
# Takes in a numlist and a value and returns the number of values that are greater than the given value
def count_greater_than(numlist, value):
   if numlist == "mt" or value == "mt":
      return 0
   if numlist.value > value:
      return (1 + count_greater_than(numlist.rest, value))
   return count_greater_than(numlist.rest, value)

# * 4:
# NumList number -> int
# Takes in a numlist and a value and returns the position of that value. 
def find(numlist, value, acc=0):
   if numlist == "mt" or value == "mt":
      return None
   else:
      if numlist.value == value:
         return acc
      else:
         return find(numlist.rest, value, acc+1)

# * 5:
# NumList -> NumList
# Takes in a numlist and returns a new numlist where every number in the new numlist is one less
def sub_one_map(numlist):
   if numlist == "mt":
      return "mt"
   else:
      return Pair(numlist.value - 1, sub_one_map(numlist.rest))

# * 6:
# SortedList number -> SortedList
# Takes in a sortedlist and a number and returns a new sortedlist with the number in the correct position
def insert(sortedlist, value):
   if sortedlist == "mt":
      return Pair(value, "mt")
   if sortedlist.rest == "mt" and sortedlist.value > value:
      return Pair(value, Pair(sortedlist.value, "mt"))
   if sortedlist.rest == "mt" and sortedlist.value < value:
      return Pair(sortedlist.value, Pair(value, "mt"))
   if sortedlist.rest.value > value and sortedlist.value < value:
      return Pair(sortedlist.value, Pair(value, sortedlist.rest))
   return Pair(sortedlist.value, insert(sortedlist.rest, value))

# * Tests : the test case class for the list functions
class Test(unittest.TestCase):
   def test_repr(self):
      self.assertEqual(repr(Pair(3, "mt")), str(Pair(3, "mt")))
   def test_length_1(self):
      self.assertEqual(length(Pair(3, "mt")), 1)
   def test_length_2(self):
      self.assertEqual(length("mt"), 0)
   def test_length_3(self):
      self.assertEqual(length(Pair(1, Pair(2, Pair(3, "mt")))), 3)
   def test_sum_1(self):
      self.assertEqual(sum(Pair(1, (Pair(2, "mt")))), 3)
   def test_sum_2(self):
      self.assertEqual(sum("mt"), 0)
   def test_sum_3(self):
      self.assertEqual(sum(Pair(5, "mt")), 5)
   def test_sum_4(self):
      self.assertEqual(sum(Pair(-5, Pair(3, "mt"))), -2)
   def test_count_greater_than_1(self):
      self.assertEqual(count_greater_than("mt", 10), 0)
   def test_count_greater_than_2(self):
      self.assertEqual(count_greater_than(Pair(5, Pair(2, "mt")), 2), 1)
   def test_count_greater_than_3(self):
      self.assertEqual(count_greater_than(Pair(2, Pair(3, "mt")), 1), 2)
   def test_count_greater_than_4(self):
      self.assertEqual(count_greater_than(Pair(2, "mt"), "mt"), 0)
   def test_count_greater_than_5(self):
      self.assertEqual(count_greater_than(Pair(-2, "mt"), -5), 1)
   def test_find_1(self):
      self.assertEqual(find(Pair(2, Pair(3, "mt")), 3), 1)
   def test_find_2(self):
      self.assertEqual(find(Pair(3, Pair(2, "mt")), 3), 0)
   def test_find_3(self):
      self.assertEqual(find(Pair(2, Pair(3, "mt")), 5), None)
   def test_find_4(self):
      self.assertEqual(find("mt", 5), None)
   def test_find_5(self):
      self.assertEqual(find(Pair(-2, "mt"), -2), 0)
   def test_find_6(self):
      self.assertEqual(find(Pair(1, Pair(2, Pair(3, Pair(4, "mt")))), 4), 3) 
   def test_find_7(self):
      self.assertEqual(find(Pair(3, "mt"), "mt"), None)
   def test_sub_one_map_1(self):
      self.assertEqual(sub_one_map(Pair(2, Pair(5, Pair(1, "mt")))), Pair(1, Pair(4, Pair(0, "mt"))))
   def test_sub_one_map_2(self):
      self.assertEqual(sub_one_map("mt"), "mt")
   def test_sub_one_map_3(self):
      self.assertEqual(sub_one_map(Pair(2, "mt")), Pair(1, "mt"))
   def test_sub_one_map_4(self):
      self.assertEqual(sub_one_map(Pair(-1, "mt")), Pair(-2, "mt"))
   def test_insert_1(self):
      self.assertEqual(insert(Pair(2, "mt"), 3), Pair(2, Pair(3, "mt")))
   def test_insert_2(self):
      self.assertEqual(insert("mt", 5), Pair(5, "mt"))
   def test_insert_3(self):
      self.assertEqual(insert(Pair(1, Pair(3, "mt")), 2), Pair(1, Pair(2, Pair(3, "mt"))))
   def test_insert_5(self):
      self.assertEqual(insert(Pair(-3, Pair(-1, "mt")), -2), Pair(-3, Pair(-2, Pair(-1, "mt"))))
   def test_insert_6(self):
      self.assertEqual(insert(Pair(22, Pair(29, Pair(77, "mt"))), 40), Pair(22,Pair(29,Pair(40,Pair(77,'mt')))))
   def test_instert_7(self):
      self.assertEqual(insert(Pair(1, "mt"), 0), Pair(0, Pair(1, "mt")))
if __name__ == '__main__':
   unittest.main()  
