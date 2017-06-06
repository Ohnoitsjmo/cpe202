# Justin Mo

# class HashTable a wrapper class and is one of 
# -- size or 
# -- list of values 
class HashTable:
    def __init__(self):
        self.size = 8 # an int
        self.list_of_vals = [None] * 8 # Python built in array

    def __repr__(self):
        return "Size: {!r}, List: {!r}".format(self.size, self.list_of_vals)

    def __eq__(self, other):
        return type(other) == HashTable and self.size == other.size and self.list_of_vals == other.list_of_vals

# class Value is one of
# -- key or 
# -- val
class Value:
    def __init__(self, key, val):
        self.key = key # hash value
        self.val = val # any value
    
    def __repr__(self):
        return "(Key: {!r}, Val: {!r})".format(self.key, self.val)

    def __eq__(self, other):
        return type(other) == Value and self.key == other.key and self.val == other.val

# None -> HashTable
# Takes in no parameters and returns an empty hash table with of initial size 8.
def empty_hash_table():
    return HashTable()

# HashTable key val -> HashTable
# Takes in a hash table and a pair of a value and its python build in hash value. Returns a new hash table with the key and value inserted at its appropriate place.
#def insert(table, key, val):
     
# HashTable key -> val 
# Takes in a hash table and a key and returns the associated value at that key.
def get(table, key):
    index = key % (len(table.list_of_vals))
    list_of_collisions = table.list_of_vals[index]
    if list_of_collisions == None:
        raise LookupError
    for each_val in list_of_collisions:
        if key == each_val.key:
            return each_val.val
    raise LookupError

# HashTable key -> HashTable
# Takes in a hash table and a key and removes the key-value pair from the hash table and returns the new hash table.
def remove(table, key):
    index = key % (len(table.list_of_vals))
    list_of_collisions = table.list_of_vals[index]
    counter = 0
    if list_of_collisions == None:
        raise LookupError
    length = len(list_of_collisions)
    for each_val in list_of_collisions:
        if key == each_val.key:
            if len(list_of_collisions) == 1:
                table.list_of_vals[index] = None
                return table
            for i in range(counter, length - 1):
                list_of_collisions[i] = list_of_collisions[i + 1]
            table.list_of_vals[index] = list_of_collisions[0:length - 1]
            return table
        counter += 1    
    raise LookupError 

# HashTable -> int
# Takes in a hash table and returns the number of items inside the hash table.
def size(table):
    size = 0
    for each_list in table.list_of_vals:
        if each_list is not None:
            for each_val in each_list:
                size += 1
    return size

# HashTable -> float
# Takes in a hash table and returns the current load factor of the table.
def load_factor(table):
    return (size(table) / len(table.list_of_vals))

# HashTable -> int 
# Takes in a hash table and returns the number of collisions that have occured during insertions into the hash table.
def collisions(table):
    collisions = 0
    for each_list in table.list_of_vals:
        if each_list is not None:
            if len(each_list) > 1:
                for each_val in range(1, len(each_list)):
                    collisions += 1
    return collisions
