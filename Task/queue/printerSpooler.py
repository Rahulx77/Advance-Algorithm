# ── Part A: Linear Queue Spooler (shows the limitation) ────
class PrinterSpoolerLinear:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.spool = [None] * capacity
        self.front = -1
        self.rear = -1

    def isEmpty(self): return self.front == -1
    def isFull(self):  return self.rear == self.capacity - 1

    def addJob(self, job):
        if self.isFull():
            print(f"  ❌ Spooler FULL (Linear limit). Rejected: '{job}'")
            return
        if self.isEmpty(): self.front = 0
        self.rear += 1
        self.spool[self.rear] = job
        print(f"  📄 Spooled  : {job}")

    def printJob(self):
        if self.isEmpty():
            print("  ✅ All jobs printed. Spooler idle.")
            return None
        job = self.spool[self.front]
        self.spool[self.front] = None
        if self.front == self.rear: self.front = self.rear = -1
        else: self.front += 1
        print(f"  🖨️  Printing : {job}")
        return job


# ── Part B: Circular Queue Spooler (overcomes the issue) ───
class PrinterSpoolerCircular:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.spool = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    def isEmpty(self): return self.count == 0
    def isFull(self):  return self.count == self.capacity

    def addJob(self, job):
        if self.isFull():
            print(f"  ❌ Spooler FULL. Rejected: '{job}'")
            return
        if self.isEmpty(): self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.spool[self.rear] = job
        self.count += 1
        print(f"  📄 Spooled  : {job}")

    def printJob(self):
        if self.isEmpty():
            print("  ✅ All jobs printed. Spooler idle.")
            return None
        job = self.spool[self.front]
        self.spool[self.front] = None
        if self.count == 1: self.front = self.rear = -1
        else: self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"  🖨️  Printing : {job}")
        return job


# ── Run Both ────────────────────────────────────────────────
print("\n" + "=" * 52)
print("         PRINTER SPOOLER — Linear")
print("=" * 52)
ps_linear = PrinterSpoolerLinear(capacity=5)
for i in range(1, 6):
    ps_linear.addJob(f"Student{i}_Assignment.pdf")

print()
ps_linear.printJob()
ps_linear.printJob()

print("\n  ⚠️  Trying to add new jobs after freeing 2 slots...")
ps_linear.addJob("Student6_Report.pdf")   # fails — rear already at end!
ps_linear.addJob("Student7_Thesis.pdf")

print("\n" + "=" * 52)
print("       PRINTER SPOOLER — Circular (Fix)")
print("=" * 52)
print("""
  Solution: Circular Queue wraps the rear pointer using
  modulo, so freed slots at the front are reused.
  50 students can keep submitting as jobs are printed —
  no slots ever go to waste!
""")

ps_circ = PrinterSpoolerCircular(capacity=5)
for i in range(1, 6):
    ps_circ.addJob(f"Student{i}_Assignment.pdf")

print()
ps_circ.printJob()
ps_circ.printJob()

print("\n  ✅ Adding new jobs — slots reused thanks to circular wrap...")
ps_circ.addJob("Student6_Report.pdf")    # wraps around — works!
ps_circ.addJob("Student7_Thesis.pdf")

print()
while not ps_circ.isEmpty():
    ps_circ.printJob()
ps_circ.printJob()  # idle state