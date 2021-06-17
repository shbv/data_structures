"""
Hashing:
    - Create key-value pair for item so that search for item's key is O(1)

Overview:
    hashed-key = hashfunc(item-key)
    index = hashed-key % hash-table-size 

Hash-table:
    - Datastructure with key,value pairs
        - hash-table-size = number-of-keys * number-of-slots-per-bucket
        - total number of hash-entries in the table is 'n'
    - Performance factors: 
        - Hash table size (=> large memory-cost also)
        - Hash function
            - easy to compute
            - uniform distribution across hash table
            - less collisions to same index
        - Collision handling method
            - linear probing (if index is filled, try index+offset)
            - quadratic probing
            - chaining (each index/bucket has a linked list / tree)
            - bucket chaining (each index/bucket has fixed number of slots. overall hashtable has fixed number of slots)
            - resizing (for e.g. when 60% of table is filled)

Implementation:
    - dict 
        - Mapping type object
        - Uses hash table for implementation
        - Stores elements as key-value pairs  (duplicates for values allowed)
        - O(1) avg-case. O(n) worst-case
        - Common functions:
            - d[key] = value
            - del d[key]
            - key in d
    - set
        - container that implements Set interface
        - Only stores values. key is same as value. (no duplicates allowed)
        - O(1) avg-case. O(n) worst-case
        - Common functions:
            - s.add(value)
            - s.remove(value)
            - key in s
    - Custom
        - Shown below

"""

class HashEntry:
    def __init__(self):
        self.key = key
        self.value = value
        self.next_entry = None
    
    def __str__(self):
        return str(self.key) + "," + str(self.value)

class HashTable:
    def __init__(self, num_slots):
        pass

    def get_index(self, key):
        pass

    def insert(self, key, value):
        pass

    def delete(self, key): 
        pass

if __name__ == '__main__':
    pass

