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
        for _ in range(index - 1):
            curr = curr.next
        return curr

    def remove_node(self, value):
        curr = self.head
        prev = None
        if self.size == 0:
            return None

        while curr.next is not None and curr.value != value:
            prev = curr
            curr = curr.next

        if not prev and curr.value == value:
            del self.head
            self.head = None
            self.size -= 1
            return curr.value

        elif curr.value == value:
            prev.next = curr.next
            self.size -= 1
            return curr.value

        return None

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next
        print("ths size of the linked list is : ", self.size)

    def find_middle_node(self):
        if self.size == 0:
            return None
        slow = self.head
        fast = self.head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return slow


linked_list = LinkeList()

linked_list.add_back(1)
linked_list.add_back(2)
linked_list.add_back(3)
linked_list.add_back(4)
linked_list.add_back(5)
linked_list.add_back(6)

# linked_list.print_list()
print(linked_list.find_middle_node())
# print()
# linked_list.print_list()
