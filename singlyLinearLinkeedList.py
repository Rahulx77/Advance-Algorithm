class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class signlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Track tail for O(1) append

    # 1. Insert at Beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:           # First node
            self.tail = new_node

    # 2. Insert at End
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node       # O(1) via tail pointer
        self.tail = new_node

    # 3. Delete from Beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty.")
            return None
        removed = self.head.data
        self.head = self.head.next
        if self.head is None:           # List became empty
            self.tail = None
        return removed

    # 4. Delete from End
    def delete_from_end(self):
        if self.head is None:
            print("List is empty.")
            return None
        removed = self.tail.data
        if self.head == self.tail:      # Only one node
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        return removed

    # 5. Traverse
    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
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
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == data:      # Target is head
            self.delete_from_beginning()
            print(f"Deleted {data} from the list.")
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:   # Target is tail
                    self.tail = current
                current.next = current.next.next
                print(f"Deleted {data} from the list.")
                return
            current = current.next
        print(f"{data} not found in the list.")


# ── Demo ──────────────────────────────────────────────────────────────────────

ll = signlyLinkedList()

print("=== Insert at End (append) ===")
ll.append(10)
ll.append(20)
ll.append(30)
ll.traverse()                           # 10 -> 20 -> 30 -> None

print("\n=== Insert at Beginning (prepend) ===")
ll.prepend(5)
ll.prepend(1)
ll.traverse()                           # 1 -> 5 -> 10 -> 20 -> 30 -> None

print("\n=== Delete from Beginning ===")
print("Removed:", ll.delete_from_beginning())   # Removed: 1
ll.traverse()                           # 5 -> 10 -> 20 -> 30 -> None

print("\n=== Delete from End ===")
print("Removed:", ll.delete_from_end())          # Removed: 30
ll.traverse()                           # 5 -> 10 -> 20 -> None

print("\n=== Search ===")
ll.search(10)                           # Found 10 at index 1.
ll.search(99)                           # 99 not found in the list.

print("\n=== Delete by Value ===")
ll.delete_by_value(10)
ll.traverse()                           # 5 -> 20 -> None