class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

hash_table = [None] * 8   # 8 slots, all initiailized to None

def my_hash(s):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers
    string_utf = s.encode()
    total = 0
    for char in string_utf:
        total += char
        total &= 0xffffffff # limit total to 32 bits
    return total

def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)

def put(key, val):
    # hash the key and get an index
    i = hash_index(key)
    # find the start of the linked list using the index
    # Search through linked list
    # IF the key already exists in the linked list
        # Replace the value
    # Else
        # Add new HashTable Entry to the head of linked list

def get(key):
    # hash the key and get an index
    i = hash_index(key)
    # Get the linked list AT the computed index
    # Search through the linked list for the key
    #   Compare keys until you find the right one
    # If it exists, return the value
    # else, return None

def delete(key):
    # hash the key and get an index
    i = hash_index(key)
    # Search through the linked list for the matching key
    # Delete that node
    # Return value of deleted node (or None)

def resize():
    # Make a new array thats DOUBLE the current size
    # Go through each linked list in the array
        # GO through each item and re-hash it
        # Insert the items into their new locations
# def shrink():
#     # Same as resize, but reduce array by HALF
#     pass
put("Hello", "Hello Value")
put("World", "World Value")​
print(hash_table)
put("foo", "Foo Value")
print(hash_table)
value = get("foo")
print(value)
print(hash_index("Hello"))
print(hash_index("foo"))