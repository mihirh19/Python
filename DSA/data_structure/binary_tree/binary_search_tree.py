from __future__ import annotations

from typing import List


class Node:
    def __init__(self, data, parent: Node = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


class Binarysearchtree:
    def __init__(self):
        self.root = None

    def empty(self):
        """
        empties the tree
        :return:
        """
        self.root = None

    def is_empty(self) -> bool:
        """
        check if the tree is empty
        :return:
        """
        return self.root is None

    def inorder(self) -> List[int]:
        result = []
        self.__inorder_helper(result, self.root)
        return result

    def __inorder_helper(self, result: List, node: Node):
        if node is not None:
            self.__inorder_helper(result, node.left)
            result.append(node.data)
            self.__inorder_helper(result, node.right)

    def insert(self, *datas) -> None:
        for dat in datas:
            self.__insert_helper(dat)

    def __insert_helper(self, data: int) -> None:
        if self.is_empty():
            self.root = Node(data)
        else:
            current = self.root
            while current is not None:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right


if __name__ == '__main__':
    t1 = Binarysearchtree()
    t1.insert(3, 1, 2, 4, 7, 6)

    print(t1.inorder())
