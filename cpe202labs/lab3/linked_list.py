# Justin Mo

# An AnyList is one of
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

# None -> None
# takes in no arguments and returns an empty list
def empty_list():
    return None

# NumList -> int
# Takes in a anylist and returns the length of the list
def length(anylist):
    if anylist == None:
        return 0
    return 1 + length(anylist.rest)

# AnyList int value -> AnyList
# takes in anylist, an index, and a value and return a new anylist with the value inserted at the given index
def add(anylist, index, value, counter=0): 
    if index == 0:
        return Pair(value, anylist)
    if index == counter and anylist == None:
        return Pair(value, None)
    if index == counter:
        return Pair(value, anylist)
    if index < 0 or anylist == None:
        raise IndexError
    return Pair(anylist.first, add(anylist.rest, index, value, counter + 1))

# AnyList int -> int
# takes in anylist and an index and returns the value at the given index
def get(anylist, index, counter=0):
    if index < 0 or anylist == None:
        raise IndexError
    if index == counter:
        return anylist.first
    return get(anylist.rest, index, counter + 1)

# AnyList int value -> AnyList
# takes in anylist, an index, and a value and returns a new list where the value at the given index is replaced by the new given value
def set(anylist, index, value, counter=0):
    if index < 0 or anylist == None:
        raise IndexError
    if index == counter:
        return Pair(value, anylist.rest)
    return Pair(anylist.first, set(anylist.rest, index, value, counter + 1))

# AnyList int -> int
# takes in anylist and an index and returns the value of that index
def remove_helper(anylist, index):
    if anylist == None:
        raise IndexError
    if index > 0 and anylist.rest == None:
        raise IndexError
    if index == 0:
        return anylist.first
    return remove_helper(anylist.rest, index - 1)

# AnyList int -> Anylist
# takes in anylist and an index and returns a new anylist with the value at the given index removed
def remove_helper2(anylist, index):
    if anylist == None:
        raise IndexError
    if index > 0 and anylist.rest == None:
        raise IndexError
    if index == 0:
        return anylist.rest
    return Pair(anylist.first, remove_helper2(anylist.rest, index - 1))

# AnyList int -> tuple
# takes in anylist and an index and returns a tuple containing the value removed and the resulting list
def remove(anylist, index):
    if anylist == None:
        raise IndexError
    if anylist.rest == None and index > 0:
        raise IndexError
    else:
        return (remove_helper(anylist, index), remove_helper2(anylist, index))

