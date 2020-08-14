class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
MAX_LF = 0.7


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = max(capacity, MIN_CAPACITY)
        self.storage = [None] * self.capacity
        self.item_count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.item_count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """                                                                                                                               
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hte = HashTableEntry(key, value)
        index = self.hash_index(key)
        curr = self.storage[index]
        if not curr:
            self.storage[index] = hte
        else:
            if curr.key == key:
                curr.value = value
            else:
                while curr.next is not None:
                    curr = curr.next
                    if curr.key == key:
                        curr.value = value
                        break
                curr.next = hte
        self.item_count += 1

        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        curr = self.storage[index]
        found = False
        if not curr:
            print('Warning, key not found')
            return
        if curr.key == key:
            if curr.next:
                self.storage[index] = curr.next
            else:
                self.storage[index] = None
            found = True
        else:
            while curr.next != key and curr.next:
                curr = curr.next
            if curr.next == key:
                curr.next = curr.next.next
                found = True
            else:
                print('Warning, key not found')
        if found:
            self.item_count -= 1
            load_factor = self.get_load_factor()
            if load_factor < 0.2:
                self.resize(self.capacity // 2)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        curr = self.storage[index]
        if not curr:
            return None
        if curr.key == key:
            return curr.value
        else:
            while curr.next:
                curr = curr.next
                if curr.key == key:
                    return curr.value
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_storage = self.storage
        old_count = self.item_count
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        for i in old_storage:
            curr = i
            while curr:
                self.put(curr.key, curr.value)
                curr = curr.next

        self.item_count = old_count
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
