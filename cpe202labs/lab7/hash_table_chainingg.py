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

# NumList -> int
# Takes in a anylist and returns the length of the list
def length(anylist):
    if anylist == None:
        return 0
    return 1 + length(anylist.rest)

# AnyList int value -> AnyList
# takes in anylist, an index, and a value and return a new anylist with the value inserted at the given index
def addd(anylist, index, value, counter=0):
    if index == 0:
        return Pair(value, anylist)
    if index == counter and anylist == None:
        return Pair(value, None)
    if index == counter:
        return Pair(value, anylist)
    if index < 0 or anylist == None:
        raise IndexError
    return Pair(anylist.first, addd(anylist.rest, index, value, counter + 1))

# AnyList int -> int
# takes in anylist and an index and returns the value at the given index
def gett(anylist, index, counter=0):
    #if index < 0 or anylist == None:
    #    raise IndexError
    if index == counter:
        return anylist.first
    return gett(anylist.rest, index, counter + 1)

# AnyList int value -> AnyList
# takes in anylist, an index, and a value and returns a new list where the value at the given index is replaced by the new given value
def sett(anylist, index, value, counter=0):
    if index < 0 or anylist == None:
        raise IndexError
    if index == counter:
        return Pair(value, anylist.rest)
    return Pair(anylist.first, sett(anylist.rest, index, value, counter + 1))

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
def removee(anylist, index):
    #if anylist == None:
    #    raise IndexError
    #if anylist.rest == None and index > 0:
    #    raise IndexError
    return (remove_helper(anylist, index), remove_helper2(anylist, index))

# class HashTable is a wrapper class and is one of
# -- size or 
# -- LinkedList of values
class HashTable:
    def __init__(self):
        self.capacity = 8 # an int
        self.size = 0 # an int
        self.collisions = 0 # an int    
        self.list_of_vals = [None] * 8 # Python built in array 
                
    def __repr__(self):
        return "Capacity: {!r}, Size: {!r}, Collisions: {!r}, List: {!r}".format(self.capacity, self.size, self.collisions, self.list_of_vals)

    def __eq__(self, other):
        return type(other) == HashTable and self.size == other.size and self.list_of_vals == other.list_of_vals and self.capacity == other.capacity and self.collisions == other.collisions

# class Item is one of
# -- key or
# -- val
class Item:
    def __init__(self, key, val):
        self.key = key # unique hash value
        self.val = val # any value

    def __repr__(self):
        return "(Key: {!r}, Val: {!r})".format(self.key, self.val)

    def __eq__(self, other):
        return type(other) == Item and self.key == other.key and self.val == other.val

# None -> HashTable
# Takes in no parameters and returns an empty hash table with of initial size 8.
def empty_hash_table():
    return HashTable()

# HashTable key val -> HashTable
# Takes in a hashtable and a pair of a value and its python build in hash value. Returns a new hash table with the key and value inserted at its appropriate place.
def insert(table, key, val):
	if load_factor(table) > 1.5:
		table = rehash(table)
	index = hash(key) % table.capacity
	list_of_collisions = table.list_of_vals[index] 
	if list_of_collisions == None:
		list_of_collisions = Pair(Item(key, val), None)
		table.list_of_vals[index] = list_of_collisions
		table.size += 1
		return table 
	else:
		table.collisions += 1
		for i in range(0, length(list_of_collisions)):
			item = gett(list_of_collisions, i)
			if item.key == key:
				list_of_collisions = sett(list_of_collisions, i, Item(key, val))
				table.list_of_vals[index] = list_of_collisions
				return table
		list_of_collisions = addd(list_of_collisions, 0, Item(key, val))
		table.list_of_vals[index] = list_of_collisions
		table.size += 1
		return table

# HashTable -> HashTable
# Takes in a HashTable with a load factor greater than 1.5 and rehashes everything and returns the rehashed HashTable.
def rehash(table):
	new_table = empty_hash_table()
	new_table.collisions = 0
	new_table.capacity = (table.capacity * 2)
	new_table.list_of_vals = [None] * new_table.capacity
	for each_list in table.list_of_vals:
		if each_list is not None:
			for i in range(0, length(each_list)):
				item = gett(each_list, i)
				insert(new_table, item.key, item.val)
	return new_table

# HashTable key -> val
# Takes in a hash table and a key and returns the associated value at that key.
def get(table, key):
    index = hash(key) % (table.capacity)
    list_of_collisions = table.list_of_vals[index]
    if list_of_collisions == None:
        raise LookupError
    for i in range(0, length(list_of_collisions)):
        item = gett(list_of_collisions, i)
        if key == item.key:
            return item.val
    raise LookupError

# HashTable key -> HashTable
# Takes in a hash table and a key and removes the key-value pair from the hash table and returns the new hash table.
def remove(table, key):
    index = hash(key) % (table.capacity)
    list_of_collisions = table.list_of_vals[index]
    if list_of_collisions == None:
        raise LookupError
    for i in range(0, length(list_of_collisions)):
        item = gett(list_of_collisions, i)
        if key == item.key:
            tple = removee(list_of_collisions, i)
            table.list_of_vals[index] = tple[1]
            table.size -= 1    
            return table
    raise LookupError
        
# HashTable -> int
# Takes in a hash table and returns the number of items inside the hash table.
def size(table):
    return table.size

# HashTable -> float
# Takes in a hash table and returns the current load factor of the table.
def load_factor(table):
    return size(table) / table.capacity

# HashTable -> int
# Takes in a hash table and returns the number of collisions that have occured during insertions into the hash table.
def collisions(table):
    return table.collisions



