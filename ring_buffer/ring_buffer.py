from sll import SinglyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = SinglyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add(item)
        else:
            self.storage.overwrite(item)

    def get(self):
        return self.storage.to_array()

buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')

print(buffer.get())   # should return []