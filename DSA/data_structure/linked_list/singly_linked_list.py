"""
Singly Linked List

A singly linked list is a data structure that consists of a sequence of nodes, where each node contains a value and a
reference to the next node in the list. The first node in the list is called the head, and the last node is called
the tail. The tail node's reference is set to None, indicating the end of the list.

Key Features of Singly Linked List:

Each node contains a value and a reference to the next node in the list.
The head points to the first node in the list, and the tail points to the last node.
The tail's reference is set to None, indicating the end of the list.
Insertion and deletion operations can be performed at the beginning, end, or at a specific index of the list.
Singly linked lists are dynamic in size, meaning they can grow or shrink as needed.
Advantages of Singly Linked List:

Efficient insertion and deletion operations at the beginning of the list, as they can be done in constant time O(1).
Efficient memory usage, as memory is allocated dynamically only for the nodes that are actually needed.
Flexibility in size, as the list can grow or shrink as needed without requiring pre-allocation of memory.
Disadvantages of Singly Linked List:

Retrieval of a specific node requires traversing the list from the head, which takes O(n) time in the worst case, where n is the number of nodes in the list.
Random access is not possible, as there is no direct reference to any node other than the head and tail.
Common Operations on Singly Linked List:

Insertion at the beginning: Adds a new node with the given value at the beginning of the list, and updates the head reference.
Insertion at the end: Adds a new node with the given value at the end of the list, and updates the tail reference.
Deletion: Removes a node with the given value from the list, and updates the references of the adjacent nodes.
Length: Returns the number of nodes in the list.
Value at index: Returns the value of the node at the specified index in the list.
Insertion at index: Adds a new node with the given value at the specified index in the list, and updates the references of the adjacent nodes.
Display: Prints the values of all the nodes in the list.
Singly linked lists are commonly used in various computer algorithms and data manipulation tasks, such as implementing stacks, queues, and hash tables. They are also useful in scenarios where dynamic memory allocation and deallocation are required, and efficient insertion and deletion operations at the beginning or end of the list are needed.
"""
from typing import Any


class Node:

    def __init__(self, data: Any):
        """
        :type data: Any
        :param data:
        create a new node with the given value
        """

        self.data: Any = data
        self.next: Node = None


class SinglyLinkedList:

    def __init__(self):
        """
        create a new empty list
        """

        self.head = None

    def __iter__(self) -> Any:
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

    def __repr__(self):
        temp = self.head

        string = ""
        while temp:
            string += f'{temp.data} -> '
            temp = temp.next

        return string[:-2]

    def __str__(self):
        temp = self.head

        string = ""
        while temp:
            string += str(temp.data) + "->"
            temp = temp.next

        return string[:-2]

    def __len__(self) -> int:

        temp = self.head
        l = 0
        while temp:
            l += 1
            temp = temp.next

        return l

    def __getitem__(self, index: int) -> Any:
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")

        for i, node in enumerate(self):
            if i == index:
                return node

        return None

    def __setitem__(self, index: int, data: Any) -> None:
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")

        node = self.head
        for i in range(index):
            node = node.next

        node.data = data

    def insert_tail(self, data: Any) -> None:
        self.insert_at_index(len(self), data)

    def insert_head(self, data: Any) -> None:
        self.insert_at_index(0, data)

    def insert_at_index(self, index: int, data: Any) -> None:
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    def delete_at_index(self, index: int) -> None:
        if index < 0 or index > len(self) - 1:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next

    def delete_tail(self) -> None:
        self.delete_at_index(len(self) - 1)

    def delete_head(self) -> None:
        self.delete_at_index(0)


if __name__ == '__main__':
    l1 = SinglyLinkedList()

    l1.insert_head(1)
    l1.insert_tail(2)
    l1.insert_tail(3)

    l1.insert_at_index(1, 4)

    print(l1)
