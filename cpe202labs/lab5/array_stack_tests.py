import unittest
from array_stack import *

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
        stack.head.array = [1, 2, 3]
        stack.head.length = 3
        self.assertEqual(repr(stack), "Stack: 1, 2, 3")

    def test_empty_stack(self):
        stack = Stack()
        self.assertEqual(empty_stack(), stack)

    def test_push(self):
        stack1 = Stack()
        stack2 = Stack()
        stack2.head.array = [1]
        stack2.head.length = 1
        stack3 = Stack()
        stack3.head.length = 3
        stack3.head.array = [1, 2, 3]
        stack4 = Stack()
        stack4.head.length = 4
        stack4.head.array = [1, 2, 3, 4]
        stack5 = Stack()
        stack5.head.length = 2
        stack5.head.array = [1, 2]
        push(stack5, 3)
        pop(stack5)
        pop(stack5)
        pop(stack5)
        push(stack5, 1)
        push(stack5, 2)
        self.assertEqual(push(stack1, 1), stack2)
        self.assertEqual(push(stack3, 4), stack4)
        

    def test_pop(self):
        stack1 = Stack()
        with self.assertRaises(IndexError):
            pop(stack1)
        stack2 = Stack()
        stack2.head.array = [1, 2, 3]
        stack2.head.length = 3
        stack3 = Stack()
        stack3.head.array = [1, 2]
        stack3.head.length = 2
        self.assertEqual(pop(stack2), (3, stack3))


    def test_peek(self):
        stack1 = Stack()
        with self.assertRaises(IndexError):
            peek(stack1)
        stack2 = Stack()
        stack2.head.array = [1, 2, 3]
        stack2.head.length = 3
        self.assertEqual(peek(stack2), 3)

    def test_size(self):
        stack1 = Stack()
        stack1.head.array = [1, 2, 3]
        stack1.head.length = 3
        self.assertEqual(size(stack1), 3)

    def test_is_empty(self):
        stack1 = Stack()
        stack2 = Stack()
        stack2.head.array = [1, 2, 3]
        stack2.head.length = 3
        self.assertTrue(is_empty(stack1))
        self.assertFalse(is_empty(stack2))
        stack3 = Stack()
        stack3.head.array = [1]
        stack3.head.length = 1
        pop(stack3)
        self.assertTrue(is_empty(stack3))
        stack4 = Stack()
        stack4.head.array = [1, 2]
        stack4.head.length = 2
        pop(stack4)
        pop(stack4)
        push(stack4, 1)
        pop(stack4)
        push(stack4, 1)
        push(stack4, 2)
        pop(stack4)
        pop(stack4)
        stack5 = Stack()
        push(stack5, 1)
        self.assertFalse(is_empty(stack5))
        pop(stack5)
        self.assertTrue(is_empty(stack5))
        stack6 = Stack()
        stack6.head.length = 3
        stack6.head.array = [1, 2, 3]
        pop(stack6)
        pop(stack6)
        push(stack6, 1)
        push(stack6, 2)
        pop(stack6)
        pop(stack6)
        pop(stack6)
        push(stack6, 1)
        push(stack6, 2)
        stack7 = Stack()
        push(stack7, 1)
        pop(stack7)
        push(stack7, 1)
        pop(stack7)
        self.assertTrue(is_empty(stack7))
        self.assertFalse(is_empty(stack6))
        stack8 = Stack()
        stack8.head.array = [1, 2, 3]
        stack8.head.length = 3
        push(stack8, 1)
        pop(stack8)
        push(stack8, 3)
        pop(stack8)
        self.assertFalse(is_empty(stack8))
        stack9 = Stack()
        stack9.head.length = 5
        stack9.head.array = [1, 2, 3, 4, 5]
        push(stack9, 6)
        pop(stack9)
        pop(stack9)
        pop(stack9)
        pop(stack9)
        pop(stack9)
        pop(stack9)
        push(stack9, 1)
        self.assertFalse(is_empty(stack9))
        stack10 = Stack()
        stack10.head.length = 5
        stack10.head.array = [1, 2, 3, 4, 5]
        pop(stack10)
        pop(stack10)
        pop(stack10)
        pop(stack10)
        pop(stack10)
        push(stack10, 1)
        stack11 = Stack()
        stack11.head.length = 10
        stack11.head.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        push(stack11, 11)
        print(stack11)
        pop(stack11)
        print(stack11)
        pop(stack11)
        pop(stack11)
        push(stack11, 1)
        self.assertFalse(is_empty(stack11))
        self.assertFalse(is_empty(stack10))

if __name__ == "__main__":
    unittest.main()
