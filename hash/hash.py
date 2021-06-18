"""
Hashing:
    - Create key-value pair for item so that search for item's key is O(1)

Overview:
    item-key' = hash(item-key)   ; # large/non-numeric to small/numeric key
    index = hashfunc(item-key')
    (e.g. index = item-key' % hash-table-size,
    or fitting into hashtable could be separated 
          index = index % hash-table-size) 

Hash-table:
    - Datastructure with key,value pairs
        - hash-table-size = number-of-keys * number-of-slots-per-bucket
        - total number of hash-entries in the table is 'n'
    - Performance factors: 
        - Hash table size 
            - large memory-cost also
        - load-factor:
            - number-of-entries / number-of-buckets
        - Hash function
            - easy to compute
            - uniform distribution across hash table
            - less collisions to same index
        - Collision handling method
            - chaining (each index/bucket has a linked list / tree)
                - bucket chaining: bucket array of fixed size (resized when load-factor exceeds threshold). each buckets has linked-list of entries 
            - open addressing (or closed hashing)
                - linear probing: if index is filled, try (index+offset)%hash-table-size  
                - quadratic probing: if index is filled, try (index+offset^2)%hash-table-size 
                - double hashing: if index is filled, try (index+offset)%hash-table-size, where offset = hashfunc2(item-key'
            - resizing (for e.g. when 60% of table is filled)

Implementation:
    - dict 
        - Mapping type object
        - Uses hash table for implementation
        - Stores elements as key-value pairs  
        - O(1) avg-case. O(n) worst-case
        - Common functions:
            - d[key] = value
            - del d[key]
            - key in d
    - set
        - container that implements Set interface
        - Only stores values. key is same as value. 
        - O(1) avg-case. O(n) worst-case
        - Common functions:
            - s.add(value)
            - s.remove(value)
            - key in s
    - Custom
        - Shown below

"""

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.key) + "," + str(self.value)

class HashTable:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.bucket = [None] * self.num_buckets # array of buckets. each bucket has linked list of entries
        self.num_entries = 0
        self.load_threshold = 0.75  # resize the table if load_factor (=num_entries/num_buckets) > load_threshold

    def get_size(self):
        return self.num_entries

    def get_index(self, key, num_buckets = None):
        if num_buckets is None:
            num_buckets = self.num_buckets
        key_p = hash(key)
        index = key_p % num_buckets  # ideally, modulo a prime number before this
        return index

    def insert(self, key, value):
        index = self.get_index(key)
        if self.bucket[index] is None:
            # create new entry
            item = HashEntry(key, value) 
            self.num_entries += 1
            self.bucket[index] = item
            print(f"Inserted ({key}, {value}) at index {index} (beginning of bucket linked list)")
        else:
            # traverse list to search for key. if no key, create new entry end of linked list
            curr_node = self.bucket[index] 
            while curr_node is not None:
                if curr_node.key == key:  # found existing key
                    curr_node.value = value
                    print(f"Updated ({key}, {value}) at index {index}")
                    break
                elif curr_node.next is None: # end of linked list
                    item = HashEntry(key, value)
                    curr_node.next = item
                    self.num_entries += 1
                    print(f"Inserted ({key}, {value}) at index {index} (end of bucket linked list)")
                    break
                curr_node = curr_node.next
        # Resize if needed
        load_factor = float(self.num_entries) / float(self.num_buckets)
        print(f"load_factor: {load_factor}")
        if load_factor >= self.load_threshold:
            self.resize()

    def delete(self, key): 
        index = self.get_index(key)
        prev_node = None
        curr_node = self.bucket[index]
        while curr_node is not None:
            if curr_node.key == key:  # found existing key
                if prev_node is None:
                    self.bucket[index] = curr_node.next
                else:
                    prev_node.next = curr_node.next
                curr_node.next = None
                self.num_entries -= 1
                print(f"Deleted ({key}, {curr_node.value}) at index {index}")
                return
            prev_node = curr_node
            curr_node = curr_node.next
        print(f"Key: {key} not found to delete")
        
    def search(self, key):
        index = self.get_index(key)
        curr_node = self.bucket[index]
        while curr_node is not None:
            if curr_node.key == key:  # found existing key
                print(f"Found ({key}, {curr_node.value}) at index {index}")
                return curr_node.value
            curr_node = curr_node.next
        print(f"Key: {key} not found")
        return None

    def resize(self):
        num_buckets_new = self.num_buckets * 2
        print(f"\t === Resizing hash table num_buckets from {self.num_buckets} to {num_buckets_new} ===")
        bucket_new = [None] * num_buckets_new
        # Traverse all entries and rehash them with new function
        for bucket in self.bucket:
            curr_node = bucket # head node
            while curr_node is not None:
                key, value = curr_node.key, curr_node.value
                ##  === Same functionality as insert ===
                index = self.get_index(curr_node.key, num_buckets_new)
                if bucket_new[index] is None:
                    # create new entry
                    item = HashEntry(key, value) 
                    print(f"\tresize(): Inserted ({key}, {value}) at index {index} (beginning of bucket linked list)")
                    bucket_new[index] = item
                else:
                    # traverse list to search for key. if no key, create new entry end of linked list
                    curr_node_new = bucket_new[index] 
                    while curr_node_new is not None:
                        if curr_node_new.key == key:  # found existing key
                            curr_node_new.value = value
                            print(f"\tresize(): Updated ({key}, {value}) at index {index}")
                            break
                        elif curr_node_new.next is None: # end of linked list
                            item = HashEntry(key, value)
                            curr_node_new.next = item
                            print(f"\tresize(): Inserted ({key}, {value}) at index {index} (end of bucket linked list)")
                            break
                        curr_node_new = curr_node_new.next
                curr_node = curr_node.next
        self.num_buckets = num_buckets_new
        self.bucket = bucket_new

if __name__ == '__main__':

    num_buckets = 8
    htable = HashTable(num_buckets)  
    print(f"htable size: {htable.get_size()}, num_buckets:{htable.num_buckets}")
    print(f"htable: {htable}")

    items = [("k1", "v1"), ("k2", "v2"), ("k3", "v3"), ("k4", "v4")]
    print(f"=== Inserting {items} ===")
    for item in items:
        htable.insert(*item)
    print(f"htable size: {htable.get_size()}, num_buckets:{htable.num_buckets}")
    print(f"htable: {htable}")

    items = [("k2", "vx")]
    print(f"=== Inserting {items}, should update ===")
    for item in items:
        htable.insert(*item)
    print(f"htable size: {htable.get_size()}")
    print(f"htable: {htable}")

    items = [("k5", "v5"), ("k6", "v6")]
    print(f"=== Inserting {items}, should resize ===")
    for item in items:
        htable.insert(*item)
    print(f"htable size: {htable.get_size()}, num_buckets:{htable.num_buckets}")
    print(f"htable: {htable}")

    keys = ["k5", "k1"]
    print(f"=== Deleting keys {items} ===")
    for key in keys:
        htable.delete(key)
    print(f"htable size: {htable.get_size()}, num_buckets:{htable.num_buckets}")
    print(f"htable: {htable}")

    keys = ["k2"]
    print("=== Search keys {items} ===")
    for key in keys:
        htable.search(key)
    print(f"htable size: {htable.get_size()}, num_buckets:{htable.num_buckets}")
    print(f"htable: {htable}")

