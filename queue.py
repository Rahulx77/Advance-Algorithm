class Queue:
    def __init__(self, capacity=6):
        self.items = []
        self.capacity = capacity

    def enqueue(self, element):
        """Insert element to the rear of the queue."""
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.items.append(element)
        print(f"Enqueued: {element}")

    def dequeue(self):
        """Remove and return element from the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        removed = self.items.pop(0)
        print(f"Dequeued: {removed}")
        return removed

    def front(self):
        """View the first element without removing it."""
        if self.is_empty():
            print("Queue is empty. No front element.")
            return None
        print(f"Front: {self.items[0]}")
        return self.items[0]

    def rear(self):
        """View the last element without removing it."""
        if self.is_empty():
            print("Queue is empty. No rear element.")
            return None
        print(f"Rear: {self.items[-1]}")
        return self.items[-1]

    def is_empty(self):
        """Return True if the queue has no elements."""
        return len(self.items) == 0

    def is_full(self):
        """Return True if the queue has reached its capacity."""
        return len(self.items) == self.capacity

    def __str__(self):
        return f"Queue: {self.items} (size={len(self.items)}/{self.capacity})"


# --- Example usage ---
q = Queue(capacity=6)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)        # Queue: [10, 20, 30]

q.front()       # Front: 10
q.rear()        # Rear: 30

q.dequeue()     # Dequeued: 10
print(q)        # Queue: [20, 30]

print(q.is_empty())  # False
print(q.is_full())   # False