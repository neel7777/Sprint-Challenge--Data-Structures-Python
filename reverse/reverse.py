class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None: #empty list
            return
        if node.next_node: #if the next node exists
            new_node = node.next_node #capture next node 
            node.next_node = prev #set the next node as the previous, effectively reversing the order
            self.reverse_list(new_node, node) #recursion, passing in the next node as well as the previous of that one, repeating the process
        else:
            self.head = node
            node.next_node = prev
