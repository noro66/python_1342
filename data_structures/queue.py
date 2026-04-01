class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.length <= 0:
            self.first = new_node
            self.last = new_node
            return True
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True
