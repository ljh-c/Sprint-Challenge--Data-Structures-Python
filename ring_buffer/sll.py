class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def insert_after(self, value):
        old_next = self.next
        self.next = Node(value, old_next)
    
    def __str__(self):
        print_next = "null" if self.next is None else self.next.value
        return f"{self.value}. -> {print_next}! "

class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node else 0
    
    def __len__(self):
        return self.length
    
    def add(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            old_tail = self.tail
            old_tail.insert_after(value)
            self.tail = old_tail.next

        self.length += 1

    def __iter__(self):
        item = self.head

        while item is not None:
            yield item.value
            item = item.next
    
    def __str__(self):
        return " ".join([str(node) for node in self])
    
    def to_array(self):
        array = [str(node) for node in self]
        return array