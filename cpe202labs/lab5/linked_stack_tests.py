import unittest
from linked_stack import *

class TestStack(unittest.TestCase):
    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)
    
    def test_repr(self):
        stack = Stack()
        stack.head = Pair(1, None)
        self.assertEqual(repr(stack), "Stack: Pair(1, None)")
    
    def test_repr_pair(self):
        linked_list = Pair(1, None)
        self.assertEqual(repr(linked_list), "Pair(1, None)")

    def test_empty_stack(self):
        stack = Stack()
        self.assertEqual(empty_stack(), stack)

    def test_push(self):
        stack1 = Stack()
        stack1.size = 1
        stack1.head = Pair(1, None)
        stack2 = Stack()
        stack2.size = 2
        stack2.head = Pair(2, Pair(1, None))
        stack3 = Stack()
        stack3.size = 0
        stack4 = Stack()
        stack4.size = 1
        stack4.head = Pair(1, None)
        self.assertEqual(push(stack1, 2), stack2)
        self.assertEqual(push(stack3, 1), stack4)

    def test_pop(self):
        stack1 = Stack()
        with self.assertRaises(IndexError):
            pop(stack1)
        stack2 = Stack()
        stack2.size = 3
        stack2.head = Pair(1, Pair(2, Pair(3, None)))
        stack3 = Stack()
        stack3.size = 2
        stack3.head = Pair(2, Pair(3, None))
        self.assertEqual(pop(stack2), (1, stack3))

    def test_peek(self):
        stack1 = Stack()
        with self.assertRaises(IndexError):
            peek(stack1)
        stack2 = Stack()
        stack2.size = 3
        stack2.head = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(peek(stack2), 1)

    def test_size(self):
        stack1 = Stack()
        self.assertEqual(size(stack1), 0)
        stack2 = Stack()
        stack2.size = 3
        stack2.head = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(size(stack2), 3)

    def test_is_empty(self):
        stack1 = Stack()
        stack1.size = 0
        self.assertTrue(is_empty(stack1))
        stack2 = Stack()
        stack2.size = 1
        stack2.head = Pair(1, None)
        self.assertFalse(is_empty(stack2))




if __name__ == "__main__":
    unittest.main()
