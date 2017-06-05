# Justin Mo

from array_stack import *
from linked_stack import *

# string -> float
# Takes in a string and calculates the expression given in postfix form and returns the value at the top of the stack.
def postfix_calc(string):
    stack = empty_stack()
    list_of_elements = string.split()
    counter = 0 
    value = 0
    for each_element in list_of_elements:
        if each_element != "+" and each_element != "-" and each_element != "/" and each_element != "*":
            counter += 1
            stack = push(stack, each_element)
        else:
            if each_element == "+":
                tple = pop(stack)
                stack = tple[1]
                value = float(tple[0])
                if (counter - 1) == 0:
                    tple = pop(stack)
                    stack = tple[1]
                    value += float(tple[0])
                    counter = 0
                else:
                    tple = pop(stack)
                    stack = tple[1]
                    value += float(tple[0])
                    counter = 0
                stack = push(stack, value)
            elif each_element == "-":
                tple = pop(stack)
                stack = tple[1]
                value = float(tple[0])
                if (counter - 1) == 0:
                    tple = pop(stack)
                    stack = tple[1]
                    value = float(tple[0]) - value
                    counter = 0
                else:
                    tple = pop(stack)
                    stack = tple[1]
                    value = float(tple[0]) - value
                    counter = 0
                stack = push(stack, value) 
            elif each_element == "*":
                tple = pop(stack)
                stack = tple[1]
                value = float(tple[0])
                if (counter - 1) == 0:
                    tple = pop(stack)
                    stack = tple[1]
                    value *= float(tple[0])
                    counter = 0
                else:
                    tple = pop(stack)
                    stack = tple[1]
                    value *= float(tple[0])
                    counter = 0
                stack = push(stack, value) 
            elif each_element == "/":
                tple = pop(stack)
                stack = tple[1]
                value = float(tple[0])
                if (counter - 1) == 0:
                    tple = pop(stack)
                    stack = tple[1]
                    value = float(tple[0]) / value
                    counter = 0
                else:
                    tple = pop(stack)
                    stack = tple[1]
                    value = float(tple[0]) / value
                    counter = 0
                stack = push(stack, value) 
    return float(peek(stack))

