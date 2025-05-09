class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort_with_insertion(self):
        dummy = Node(0)
        current = self.head
        while current:
            next_node = current.next
            prev = dummy
            while prev.next and prev.next.data < current.data:
                prev = prev.next
            current.next = prev.next
            prev.next = current
            current = next_node
        self.head = dummy.next
        return dummy.next
    
    def concatenate(self, other):
        if self.head is None:
            self.head = other.head
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = other.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

linked_list_a = LinkedList()
linked_list_a.insert_at_end(25)
linked_list_a.insert_at_end(15)
linked_list_a.insert_at_end(45)
linked_list_a.insert_at_end(35)
linked_list_a.insert_at_end(65)
linked_list_a.insert_at_end(55)

linked_list_b = LinkedList()
linked_list_b.insert_at_end(20)
linked_list_b.insert_at_end(30)
linked_list_b.insert_at_end(40)
linked_list_b.insert_at_end(50)
linked_list_b.insert_at_end(60)
linked_list_b.insert_at_end(70)

linked_list_a.reverse()
print("Reversed linked list A:")
linked_list_a.print_list()

linked_list_a.sort_with_insertion()
print("Sorted linked list A:")
linked_list_a.print_list()

linked_list_a.concatenate(linked_list_b)
print("Linked list A concatenated with linked list B:")
linked_list_a.print_list()
