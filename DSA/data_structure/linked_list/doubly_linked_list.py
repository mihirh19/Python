"""A doubly linked list is a type of data structure where each node contains a data element and two pointers,
one pointing to the next node and one pointing to the previous node. This allows for traversal in both directions,
making it more versatile than a singly linked list.

Node Class
In a doubly linked list, each node contains three elements:

data: The data element stored in the node.
next: A pointer to the next node in the list.
prev: A pointer to the previous node in the list.
"""
from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        return sum(1 for i in self)

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

    def __repr__(self):
        temp = self
        string = ""
        for node in temp:
            string += f"{node} -> "

        return string[:-3]

    def insert_at_index(self, index: int, data: Any) -> None:
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        elif index == len(self):
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next

            new_node.prev = temp.prev
            new_node.next = temp
            temp.prev.next = new_node
            temp.prev = new_node

    def delete_at_index(self, index: int) -> None:
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        if len(self) == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == len(self) - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.next.prev = temp.prev
            temp.prev.next = temp.next

    def insert_head(self, data: Any) -> None:
        self.insert_at_index(0, data)

    def insert_tail(self, data: Any) -> None:
        self.insert_at_index(len(self), data)

    def delete_head(self) -> None:
        self.delete_at_index(0)

    def delete_tail(self) -> None:
        self.delete_at_index(len(self) - 1)


if __name__ == '__main__':
    l1 = DoublyLinkedList()
    l1.insert_head(1)
    l1.insert_tail(2)
    l1.insert_tail(3)
    l1.insert_at_index(2, 4)

    l1.delete_tail()
    print(l1)
