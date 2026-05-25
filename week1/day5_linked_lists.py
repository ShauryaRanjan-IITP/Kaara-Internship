class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, val):

        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node

    def delete(self, val):

        if not self.head:
            return

        if self.head.val == val:
            self.head = self.head.next
            return

        curr = self.head

        while curr.next and curr.next.val != val:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

    def display(self):

        curr = self.head

        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

        print("None")