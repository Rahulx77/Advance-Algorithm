class PriorityQueue:
    def __init__(self):
        # Each entry: (priority, order, data)
        # Higher number = higher priority
        self.queue = []
        self.order = 0    # FIFO tie-breaker

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item, priority):
        entry = (priority, self.order, item)
        self.queue.append(entry)
        self.order += 1
        print(f"  Admitted : '{item}'  priority={priority}")

    def dequeue(self):
        if self.isEmpty():
            print("  No patients in queue.")
            return None
        # Find highest priority; tie → smallest order (FIFO)
        best_idx = 0
        for i in range(1, len(self.queue)):
            curr_p, curr_o, _ = self.queue[i]
            best_p, best_o, _ = self.queue[best_idx]
            if curr_p > best_p or (curr_p == best_p and curr_o < best_o):
                best_idx = i
        priority, _, item = self.queue.pop(best_idx)
        print(f"  Treating : '{item}'  priority={priority}  ← highest priority served first")
        return item

    def peek(self):
        if self.isEmpty():
            print("  Queue is empty.")
            return None
        best = max(self.queue, key=lambda x: (x[0], -x[1]))
        print(f"  Next up  : '{best[2]}'  priority={best[0]}")

    def display(self):
        if self.isEmpty():
            print("  Waiting room is empty.")
        else:
            sorted_q = sorted(self.queue, key=lambda x: (-x[0], x[1]))
            print("  Waiting  :", [(x[2], f"P{x[0]}") for x in sorted_q])


# ── Demo: Hospital ER ───────────────────────────────────────
print("\n" + "=" * 52)
print("        PRIORITY QUEUE — Hospital ER")
print("=" * 52)
print("""
  Real-World Scenario:
  ────────────────────
  In a hospital ER patients are NOT treated in arrival
  order — a heart-attack patient jumps ahead of someone
  with a minor cut. Each patient is assigned a triage
  priority (3=Critical, 2=Moderate, 1=Minor). The queue
  always serves the highest priority first; equal
  priorities follow FIFO (who arrived first).

  Same concept in CPU Scheduling: OS assigns priority
  levels to processes. A system interrupt (P=10) preempts
  a background download (P=1) immediately.
""")

er = PriorityQueue()
er.enqueue("Alice  (sprained ankle)",  priority=1)
er.enqueue("Bob    (chest pain)",      priority=3)
er.enqueue("Carol  (high fever)",      priority=2)
er.enqueue("David  (car accident)",    priority=3)

print()
er.display()
print()
er.dequeue()   # Bob — critical, arrived first
er.dequeue()   # David — critical, arrived second (FIFO tie-break)
er.dequeue()   # Carol — moderate
er.dequeue()   # Alice — minor
er.dequeue()   # empty edge case