class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at Beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # 2. Insert at End
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # 3. Delete from Beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty.")
            return None
        removed = self.head.data
        if self.head == self.tail:      # Only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None       # Unlink old head
        return removed

    # 4. Delete from End
    def delete_from_end(self):
        if self.tail is None:
            print("List is empty.")
            return None
        removed = self.tail.data
        if self.head == self.tail:      # Only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None       # Unlink old tail
        return removed

    # 5. Traverse (Forward & Backward)
    def traverse_forward(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        if self.tail is None:
            print("List is empty.")
            return
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    # 6. Search
    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                print(f"Found {data} at index {index}.")
                return True
            current = current.next
            index += 1
        print(f"{data} not found in the list.")
        return False

    # Bonus: Delete by Value
    def delete_by_value(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                print(f"Deleted {data} from the list.")
                return
            current = current.next
        print(f"{data} not found in the list.")


# ── Demo ──────────────────────────────────────────────────────────────────────

dll = DoublyLinkedList()

print("=== Insert at End (append) ===")
dll.append(10)
dll.append(20)
dll.append(30)
dll.traverse_forward()          # 10 <-> 20 <-> 30 <-> None

print("\n=== Insert at Beginning (prepend) ===")
dll.prepend(100)
dll.traverse_forward()          # 1 <-> 5 <-> 10 <-> 20 <-> 30 <-> None

print("\n=== Traverse Backward ===")
dll.traverse_backward()         # 30 <-> 20 <-> 10 <-> 5 <-> 1 <-> None

print("\n=== Delete from Beginning ===")
print("Removed:", dll.delete_from_beginning())   # Removed: 1
dll.traverse_forward()          # 5 <-> 10 <-> 20 <-> 30 <-> None

print("\n=== Delete from End ===")
print("Removed:", dll.delete_from_end())          # Removed: 30
dll.traverse_forward()          # 5 <-> 10 <-> 20 <-> None

print("\n=== Search ===")
dll.search(10)                  # Found 10 at index 1.
dll.search(99)                  # 99 not found in the list.

print("\n=== Delete by Value ===")
dll.delete_by_value(10)
dll.traverse_forward()          # 5 <-> 20 <-> None