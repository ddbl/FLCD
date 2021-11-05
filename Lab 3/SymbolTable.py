# Capacity for internal array
INITIAL_CAPACITY = 17


# Node data structure - essentially a LinkedList node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)


class SymbolTable:
    def __init__(self):
        self.size = 0
        self.capacity = INITIAL_CAPACITY
        self.table = [None] * self.capacity

    # Generate a hash for a given value
    # Input:  value - string
    # Output: Sum of ASCII code chars modulo capacity - int
    def hash(self, value):
        string_value = str(value)
        return sum(bytearray(string_value.encode("ascii"))) % self.capacity

    # Insert a value to the hashtable
    # Input:  value - anything
    # Output: void
    def insert(self, value):
        # 1. Increment size
        self.size += 1
        # 2. Compute index of value
        index = self.hash(value)
        # Go to the node corresponding to the hash
        node = self.table[index]
        # 3. If list is empty:
        if node is None:
            # Create node, add it, return
            self.table[index] = Node(value)
            return index
        # 4. Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided value
        prev.next = Node(value)
        return index

    # Find data based on value
    # Input:  value - string
    # Output: index - int
    def find(self, value):
        # 1. Compute hash
        index = self.hash(value)
        # 2. Go to first node in list
        node = self.table[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.value != value:
            node = node.next
        # 4. Now, node is the requested value or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return index
            return index

    def __str__(self):
        # return str(self.table)
        output = ""
        for i in range(len(self.table)):
            node = self.table[i]
            output += f"{i} - "
            if node is None:
                output += "[]\n"
            else:
                while node is not None:
                    output += f"{node}; "
                    node = node.next
                output += "\n"
        return output



