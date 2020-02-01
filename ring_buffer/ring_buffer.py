from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        elif self.current is self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.current.prev
        elif self.current is self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        else:
            self.current.insert_after(item)
            self.current.delete()
            self.current = self.current.prev

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current = self.storage.head
        while current != None:
            list_buffer_contents.insert(0, current.value)
            if current.next == None:
                break
            else:
                current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
