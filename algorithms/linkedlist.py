class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = Node(data)

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        prev = None

        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        if prev is None:
            self.head = cur_node.next
        else:
            prev.next = cur_node.next

    def has_loop(self):
        slow_node = self.head
        fast_node = self.head

        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

            if slow_node == fast_node:
                return True

        return False
    def rotate_list(self, k):
        if not self.head or k <= 0:
            return

        current = self.head
        count = 1
        while current and count < k:
            current = current.next
            count += 1

        if current is self.head:
            return

        prev = self.head
        while prev.next is not current:
            prev = prev.next
        prev.next = current.next
        current.next = self.head
        self.head = current

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(50)
    ll.append(70)
    ll.append(40)
    ll.append(60)
    ll.print_list()



    print(ll.has_loop())

    ll.rotate_list(3)
    ll.print_list()