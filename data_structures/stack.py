class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = None(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end=", ")
            temp = temp.next


my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)