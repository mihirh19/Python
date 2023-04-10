class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


def display(tree: Node) -> None:
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    display(root)
