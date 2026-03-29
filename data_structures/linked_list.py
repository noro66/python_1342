class ListNode:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class LinkeList:
    def __init__(self) -> None:
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self.size: int = 0

    def add_back(self, value):
        node = ListNode(value)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        self.size += 1

    def get_node(self, index: int):
        if self.size <= 0:
            return (None)
        if self.size <= index:
            return (None)
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next
        print("ths size of the linked list is : ", self.size)


linked_list = LinkeList()

linked_list.add_back(1)
linked_list.add_back(2)
linked_list.add_back(3)
linked_list.add_back(4)
linked_list.add_back(5)
linked_list.add_back(6)

# linked_list.print_list()
print(linked_list.get_node(4))
