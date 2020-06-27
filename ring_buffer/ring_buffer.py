from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        #captures the oldest element
        self.oldest = None
        #use the doublelinkedlist as our data structure 
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity: #not at capacity
            self.oldest = self.storage.head
            self.storage.add_to_tail(item)
        else: #at capacity
            self.oldest.value = item #replace oldest value with new item

            if self.oldest is not self.storage.tail: 
               self.oldest = self.oldest.next
            else:
                self.oldest = self.storage.head #reassigning the oldest value to be the actual oldest element rather than the newly added item

    def get(self):
        content = []
        node = self.storage.head

        while node is not None:
            content.append(node.value)
            node = node.next
        return content