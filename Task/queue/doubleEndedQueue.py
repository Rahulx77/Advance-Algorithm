class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    def isEmpty(self):  return self.count == 0
    def isFull(self):   return self.count == self.capacity

    def insertFront(self, item):
        if self.isFull():
            print(f"  Deque full! Cannot insert '{item}' at front.")
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = item
        self.count += 1
        print(f"  InsertFront: {item}  → {self._view()}")

    def insertRear(self, item):
        if self.isFull():
            print(f"  Deque full! Cannot insert '{item}' at rear.")
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.count += 1
        print(f"  InsertRear : {item}  → {self._view()}")

    def deleteFront(self):
        if self.isEmpty():
            print("  Deque is empty! Cannot delete from front.")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.count == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"  DeleteFront: {item}  → {self._view()}")
        return item

    def deleteRear(self):
        if self.isEmpty():
            print("  Deque is empty! Cannot delete from rear.")
            return None
        item = self.queue[self.rear]
        self.queue[self.rear] = None
        if self.count == 1:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.capacity
        self.count -= 1
        print(f"  DeleteRear : {item}  → {self._view()}")
        return item

    def _view(self):
        if self.isEmpty(): return "[]"
        result, i = [], self.front
        for _ in range(self.count):
            result.append(str(self.queue[i]))
            i = (i + 1) % self.capacity
        return "[" + " | ".join(result) + "]  front←  →rear"


# ── Demo ───────────────────────────────────────────────────
print("\n" + "=" * 52)
print("          DOUBLE-ENDED QUEUE DEMO")
print("=" * 52)
print("""
  Insight — Deque as Stack AND Queue simultaneously:
  ──────────────────────────────────────────────────
  AS A STACK  → use only one end (insertRear + deleteRear)
                Last-In First-Out behaviour.
  AS A QUEUE  → use both ends (insertRear + deleteFront)
                First-In First-Out behaviour.
  A Deque combines both because it has NO restriction
  on which end you insert or remove from.
""")

dq = Deque(6)
dq.insertRear(10)
dq.insertRear(20)
dq.insertFront(5)
dq.insertFront(1)
dq.deleteRear()
dq.deleteFront()