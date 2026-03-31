class ListNode:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value) -> None:
        node = ListNode(value)
        self.head = node
        self.tail = node
        self.size: int = 1

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

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

    def partition_list(self, num):
        if not self.head:
            return None
        dum1 = ListNode(0)
        dum2 = ListNode(0)
        prev1 = dum1
        prev2 = dum2
        curr = self.head
        while curr:
            if curr.value < num:
                prev1.next = curr
                prev1 = curr
            else:
                prev2.next = curr
                prev2 = curr
            curr = curr.next
        prev1.next = dum2.next
        prev2.next = None
        self.head = dum1.next

    def reverse_between(self, start_index, end_index):
        if self.size == 1 or not self.head:
            return None
        dumy = ListNode(0)
        dumy.next = self.head
        prev = dumy
        for _ in range(start_index):
            prev = prev.next
        curr = prev.next
        for _ in range(end_index - start_index):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        self.head = dumy.next

    def swap_pairs(self):
        if not self.head:
            return
        dumy = ListNode(0)
        dumy.next = self.head
        prev = dumy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        self.head = dumy.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

linked_list.swap_pairs()
print("swap pairs : ")
linked_list.print_list()
