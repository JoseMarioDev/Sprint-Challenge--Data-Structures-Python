from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if ring isn't full add to ring set to tail
        if self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
            # also set to head
            self.current = self.storage.head
        # if ring is full delete head
        elif self.capacity == self.storage.length:
            # head is oldest item in ring
            oldest_item = self.storage.head
            # delete head
            self.storage.remove_from_head()
            # add item to tail
            self.storage.add_to_tail(item)
            # if only 1 item in ring, set to head and tail
            if oldest_item == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # add first item
        first_item = self.current
        list_buffer_contents.append(first_item.value)

        # check to see if there is next item
        if first_item.next:
            next_item = first_item.next
        else:
            next_item = self.storage.head

        # loop through dll, appending items till done
        while next_item is not first_item:
            list_buffer_contents.append(next_item.value)
            if next_item.next:
                next_item = next_item.next
            else:
                next_item = self.storage.head
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
