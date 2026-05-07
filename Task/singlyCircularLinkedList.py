class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    # Insert after a given node value
    def insert_after(self, target, data):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while True:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"Node with value {target} not found.")

    # Delete a node by value
    def delete(self, data):
        if not self.head:
            print("List is empty.")
            return

        temp = self.head
        prev = None

        # Find the last node to fix the circular link if needed
        last = self.head
        while last.next != self.head:
            last = last.next

        while True:
            if temp.data == data:
                if prev is None:  # Deleting head
                    if temp.next == self.head:  # Only one node
                        self.head = None
                    else:
                        last.next = temp.next
                        self.head = temp.next
                else:
                    prev.next = temp.next
                print(f"Node {data} deleted.")
                return
            prev = temp
            temp = temp.next
            if temp == self.head:
                break
        print(f"Node with value {data} not found.")

    # Search for a value
    def search(self, data):
        if not self.head:
            return False
        temp = self.head
        while True:
            if temp.data == data:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    # Display the list
    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        elements = []
        while True:
            elements.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(elements) + " -> (back to head)")

    # Length of the list
    def length(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            count += 1
        return count


# ─── Demo ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cll = CircularLinkedList()

    print("=== Insert at End ===")
    for val in [10, 20, 30, 40]:
        cll.insert_at_end(val)
    cll.display()

    print("\n=== Insert at Beginning ===")
    cll.insert_at_beginning(5)
    cll.display()

    print("\n=== Insert after 20 ===")
    cll.insert_after(20, 25)
    cll.display()

    print("\n=== Delete 25 ===")
    cll.delete(25)
    cll.display()

    print("\n=== Delete Head (5) ===")
    cll.delete(5)
    cll.display()

    print("\n=== Search ===")
    print("Search 30:", cll.search(30))
    print("Search 99:", cll.search(99))

    print("\n=== Length ===")
    print("Length:", cll.length())