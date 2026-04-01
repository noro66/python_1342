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