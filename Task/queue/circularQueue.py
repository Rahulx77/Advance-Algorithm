class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0      # track actual elements

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def enqueue(self, item):
        if self.isFull():
            print(f"  Queue is FULL! Cannot enqueue '{item}'")
            return
        if self.isEmpty():
            self.front = 0
        # ✅ Modulo wraps rear back to 0 when it reaches the end
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.count += 1
        print(f"  Enqueued: {item}  [front={self.front}, rear={self.rear}]")

    def dequeue(self):
        if self.isEmpty():
            print("  Queue is EMPTY! Nothing to dequeue.")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.count == 1:
            self.front = self.rear = -1
        else:
            # ✅ front also wraps around — reusing freed slots!
            self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"  Dequeued: {item}  [front={self.front}, rear={self.rear}]")
        return item

    def display(self):
        print(f"  Array : {self.queue}")
        print(f"  Count : {self.count}/{self.capacity}  front={self.front}  rear={self.rear}")


# ── Demo ───────────────────────────────────────────────────
print("\n" + "=" * 52)
print("           CIRCULAR QUEUE DEMO")
print("=" * 52)
print("""
  How it solves Linear Queue's memory waste:
  ─────────────────────────────────────────
  Linear  → rear stuck at end, freed front slots ignored.
  Circular→ rear = (rear+1) % capacity  wraps rear to 0,
            front= (front+1)% capacity  wraps front too.
  Result  → every slot is reusable, zero waste!
""")

cq = CircularQueue(5)
cq.enqueue("A")
cq.enqueue("B")
cq.enqueue("C")
cq.dequeue()
cq.dequeue()
cq.display()        # slots 0 & 1 freed

cq.enqueue("D")
cq.enqueue("E")
cq.enqueue("F")     # wraps rear to index 0 — reuses freed slot!
cq.display()