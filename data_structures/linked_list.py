class ListNode:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class LinkeList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size: int = 0

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def add_back(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            self.tail = new_node
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
        while fast and fast != self.tail:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast != self.tail:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_kth_from_end(self, kth):
        slow = self.head
        fast = self.head

        for _ in range(kth):
            if not fast:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow

    def remove_duplicates(self):
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.value in seen:
                prev.next = current.next
                self.size -= 1
            else:
                seen.add(current.value)
                prev = current
            current = current.next
        # while current:
        # runner = current
        # while runner:
        #     if runner.next and current.value == runner.next.value:
        #         runner.next = runner.next.next
        #         self.size -= 1
        #     else:
        #         runner = runner.next
        # current = current.next

    def binary_to_decimal(self):
        res = 0
        curr = self.head
        while curr:
            res = res * 2 + curr.value
            curr = curr.next
        return res


linked_list = LinkeList()

linked_list.append(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
linked_list.append(1)
linked_list.append(1)

print(linked_list.binary_to_decimal())
