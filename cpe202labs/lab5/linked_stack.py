# Justin Mo

# Stack is a wrapper class 
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        return "Stack: {!r}".format(self.head)

    def __eq__(self, other):
        return type(other) == Stack and self.head == other.head and self.size == other.size

# A LinkedList is one of
# -- "None" or
# -- Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first # any value
        self.rest = rest # anylist

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest

# None -> Stack
# Takes no arguments and returns an empty stack.
def empty_stack():
    return Stack()

# Stack int -> Stack
# Takes in a Stack and a value and adds the value to the top of the stack and returns the resulting stack.
def push(stack, value):
    if stack.head == None:
        stack.size += 1
        stack.head = Pair(value, None)
        return stack
    else:
        stack.size += 1
        stack.head = Pair(value, stack.head)
        return stack

# Stack -> tuple(int, Stack)
# Takes in a Stack and removes the top element and returns a 2-tuple of the removed element and the new Stack.
def pop(stack):
    if stack.head == None:
        raise IndexError
    else:
        stack.size -= 1
        value = stack.head.first
        stack.head = stack.head.rest    
        return (value, stack)

# Stack -> int
# Takes in a Stack and returns the top element of the Stack.
def peek(stack):
    if stack.head == None:
        raise IndexError
    else:
        return stack.head.first

# Stack -> int
# Takes in a Stack and returns the number of elements in the Stack.
def size(stack):
    return stack.size

# Stack -> bool
# Takes in a Stack and returns a bool depending on whether the stack is empty.
def is_empty(stack):
    return stack == empty_stack()






