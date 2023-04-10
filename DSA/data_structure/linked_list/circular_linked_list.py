"""Circular Linked List A circular linked list is a type of data structure where each node contains a data element
and a pointer to the next node in the list. Unlike a singly linked list, the last node's next pointer points back to
the head of the list, forming a loop. This allows for traversal in a circular manner, where the last node connects
back to the first node, creating a circular structure.

Node Class
In a circular linked list, each node contains two elements:

data: The data element stored in the node.
next: A pointer to the next node in the list.
"""
from typing import Any, Iterator


class Node:
    def __init__(self, data):
        self.data: Any = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self) -> Iterator[Any]:
        temp = self.head
        while self.head:
            yield temp.data
            temp = temp.next
            if temp == self.head:
                break

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __repr__(self):
        string = ""
        for node in self:
            string += f"{node} -> "

        return string[:-3]

    def insert_at_index(self, index: int, data: Any) -> None:
        if index < 0 or index > len(self):
            raise IndexError(f"Index {index} is out of range")

        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = self.tail.next = new_node
        elif index == len(self):
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def insert_head(self, data: Any) -> None:
        self.insert_at_index(0, data)

    def insert_tail(self, data: Any) -> None:
        self.insert_at_index(len(self), data)

    def delete_at_index(self, index: int) -> None:
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        if self.head == self.tail:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            if index == len(self) - 1:
                self.tail = temp
            temp.next = temp.next.next

    def delete_head(self) -> None:
        self.delete_at_index(0)

    def delete_tail(self) -> None:
        self.delete_at_index(len(self) - 1)


if __name__ == '__main__':
    l1 = CircularLinkedList()

    l1.insert_head(1)
    l1.insert_tail(2)
    l1.insert_head(3)
    l1.insert_tail(4)
    l1.insert_at_index(2, 7)
    print(l1)

    print("After deleting")
    l1.delete_tail()
    l1.delete_head()

    print(l1)
