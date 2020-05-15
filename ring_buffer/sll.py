class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def insert_after(self, value):
        old_next = self.next
        self.next = Node(value, old_next)
    
    # def __str__(self):
    #     print_next = "null" if self.next is None else self.next.value
    #     return f"{self.value}. -> {print_next}! "

class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.oldest = self.head
        self.length = 1 if node else 0
    
    def __len__(self):
        return self.length
    
    def add(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.tail.next = self.head
            self.oldest = self.head
        else:
            old_tail = self.tail
            old_tail.insert_after(value)
            self.tail = old_tail.next
            self.tail.next = self.head

        self.length += 1

    def overwrite(self, value):
        self.oldest.value = value
        self.oldest = self.oldest.next

    def __iter__(self):
        item = self.head

        yield item.value

        while item.next is not self.head:
            item = item.next
            yield item.value
    
    def to_array(self):
        array = [node for node in self]
        return array