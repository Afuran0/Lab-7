class Node:
    # Empty constructor
    def __init__(self, value=None, next=None, previous=None):
        self._value = value
        self._next = next
        self._previous = previous
        return

    def set(self, value):
        self._value = value
        return self

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def get_previous(self):
        return self._previous

    def set_next(self, next):
        self._next = next
        return self

    def set_previous(self, previous):
        self._previous = previous
        return self


# Creating print statements for the nodes
node1 = Node()
node2 = Node()
node3 = Node()

# Set values
node1.set(5)
node2.set(10)
node3.set(15)

# Link nodes
node1.set_next(node2)
node2.set_previous(node1)
node2.set_next(node3)
node3.set_previous(node2)

# Print outputs
print("Node 1 value:", node1.get_value())
print("Node 2 value:", node2.get_value())
print("Node 3 value:", node3.get_value())

# Traverse to following node
print("Node 1's next value:", node1.get_next().get_value())

# Traverse to previous node
print("Node 3's previous value:", node3.get_previous().get_value())
