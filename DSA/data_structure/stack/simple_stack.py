from typing import Any


class Stack:
    """
    In this implementation, the Stack class has the following additional features:

capacity: Represents the maximum capacity of the stack, which can be set during initialization or defaults to 10 if not specified.
is_full(): Returns True if the stack is full (reached its capacity), and False otherwise.
_resize(new_capacity): Private method that resizes the stack to a new capacity. It is called when the stack is full or less than 25% filled, and it doubles the capacity when expanding and halves the capacity when shrinking.
This implementation ensures that the stack dynamically resizes its capacity as needed to efficiently utilize memory space. It also includes custom exception handling for empty stack and full stack scenarios. Note that the time complexity for most stack operations, such as push(), pop(), and peek(), is still O(1) on average, making it efficient for most use cases.
    """

    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._items = [None] * self._capacity

    def __len__(self) -> int:
        """It gives the length of the stack"""
        return self._size

    def __sizeof__(self):
        return self._capacity

    def __str__(self):
        return f"this stack has capacity {self._capacity}"

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def push(self, item) -> None:
        """

        :param item:
        :return:
        """
        if self.is_full():
            self._resize(2 * self._capacity)  # Double the capacity if full
        self._items[self._size] = item
        self._size += 1

    def pop(self) -> Any:
        if not self.is_empty():
            item = self._items[self._size - 1]
            self._size -= 1
            if self._size <= self._capacity // 4:  # Shrink the capacity if less than 25% filled
                self._resize(self._capacity // 2)
            return item
        else:
            raise IndexError("Stack is empty")

    def peek(self) -> Any:
        if not self.is_empty():
            return self._items[self._size - 1]
        else:
            raise IndexError("Stack is empty")

    def _resize(self, new_capacity) -> None:
        new_items = [None] * new_capacity
        for i in range(self._size):
            new_items[i] = self._items[i]
        self._capacity = new_capacity
        self._items = new_items


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())

    print(len(s))
    print(s)
