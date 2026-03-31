class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            new_node = self.head
            new_node = self.tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        last_node = self.tail

        if self.length == 1:
            self.head == None
            self.tail == None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            last_node.prev = None
        self.length -= 1
        return last_node

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if not self.head:
            return None
        node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        self.length -= 1
        return node

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = None
        temp.next = None
        return temp

    def is_palindrome(self):
        if self.length == 2:
            return True
        forward = self.head
        backward = self.tail
        for _ in range(self.length // 2):
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
        return True

    def reverse(self):
        if self.length < 2:
            return
        current = self.head
        temp = current.prev
        for _ in range(self.length):
            current.prev = current.next
            current.next = temp
            temp = current
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        if not self.head:
            return
        dumy1 = Node(0)
        dumy2 = Node(0)
        prev1 = dumy1
        prev2 = dumy2
        curr = self.head
        for _ in range(self.length):
            if curr.value < x:
                prev1.next = curr
                curr.prev = prev1
                prev1 = prev1.next
            else:
                prev2.next = curr
                curr.prev = prev2
                prev2 = prev2.next
            curr = curr.next
        if dumy2.next:
            prev1.next = dumy2.next
            prev2.next = None
            dumy2.next.prev = prev1
        else:
            prev1.next = None
        self.head = dumy1.next
        self.head.prev = None
