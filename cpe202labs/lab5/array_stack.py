# Justin Mo

# Stack is a wrapper class
class Stack:
    def __init__(self):
        self.head = List()
    
    def __repr__(self):
        return "Stack: {!r}".format(self.head)

    def __eq__(self, other):
        return type(other) == Stack and self.head == other.head

# ArrayList is one of
# -- None or 
# -- List
class List:
    def __init__(self):
        self.array = [None]*5001 # an array list
        self.capacity = 10 # an int
        self.length = 0 # an int

    def __repr__(self):
        c = "{:s}".format(str(self.array[0]))
        for i in self.array[1:self.length]:
            c += ", {:s}".format(str(i))
        return c

    def __eq__(self, other):
            bool = True
            for i in range(0, self.length):
                if self.array[i] != other.array[i]:
                    bool = False
            return type(other) == List and bool and self.capacity == other.capacity and self.length == other.length

# None -> Stack
# Takes no arguments and returns an empty stack.
def empty_stack():
    return Stack()

# Stack int -> Stack
# Takes in a Stack and a value and adds the value to the top of the stack and returns the resulting stack.
def push(stack, value):
    if stack.head.length == 0:
        stack.head.length += 1
        stack.head.array = [value]
        return stack
    else:
        stack.head.length += 1
        stack.head.array.append(value)
        return stack

# Stack -> tuple(int, Stack)
# Takes in a Stack and removes the top element and returns a 2-tuple of the removed element and the new Stack.
def pop(stack):
    if stack == empty_stack():
        raise IndexError
    elif stack.head.length == 1:
        value = stack.head.array[0]
        stack.head.length = 0
        stack.head.array = [None]*5001
        return (value, stack)
    else:
        stack.head.length -= 1
        value = stack.head.array[stack.head.length]
        stack.head.array = stack.head.array[0: stack.head.length]
        return (value, stack)

# Stack -> int
# Takes in a Stack and returns the top element of the Stack.
def peek(stack):
    if stack == empty_stack():
        raise IndexError
    return stack.head.array[stack.head.length - 1]

# Stack -> int
# Takes in a Stack and returns the number of elements in the Stack.
def size(stack):
    return stack.head.length

# Stack -> bool
# Takes in a Stack and returns a bool depending on whether the stack is empty.
def is_empty(stack):
    return stack == empty_stack()




