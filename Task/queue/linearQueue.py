class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        # ⚠️ Static Array Limitation:
        # Even if front has moved forward (slots freed by dequeue),
        # we can't reuse them — rear hitting the last index = "full"
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.isFull():
            print(f"  Queue is FULL! Cannot enqueue '{item}'")
            print("  ⚠️  Static Limitation: freed front slots cannot be reused.")
            return
        if self.isEmpty():
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item
        print(f"  Enqueued: {item}  [front={self.front}, rear={self.rear}]")

    def dequeue(self):
        if self.isEmpty():
            print("  Queue is EMPTY! Nothing to dequeue.")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None   # clear slot (but can't reuse it!)
        if self.front == self.rear:     # last element removed
            self.front = self.rear = -1
        else:
            self.front += 1
        print(f"  Dequeued: {item}  [front={self.front}, rear={self.rear}]")
        return item

    def display(self):
        if self.isEmpty():
            print("  Queue: []")
        else:
            print(f"  Queue: {self.queue}  ← slots before index {self.front} are wasted")


# ── Demo ───────────────────────────────────────────────────
print("=" * 52)
print("            LINEAR QUEUE DEMO")
print("=" * 52)

lq = LinearQueue(5)
lq.enqueue("A")
lq.enqueue("B")
lq.enqueue("C")
lq.display()

lq.dequeue()
lq.dequeue()
lq.display()   # slots 0 & 1 are wasted

lq.enqueue("D")
lq.enqueue("E")
lq.enqueue("F")   # rear = 4 → FULL, even though 2 slots are free at front!