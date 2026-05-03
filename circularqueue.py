class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!")
            return False
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        data = self.queue[self.front]
        self.queue[self.front] = None
        if self.size == 1:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue:", self.queue)
        print(f"Front: {self.front}, Rear: {self.rear}, Size: {self.size}")


# --- Usage ---
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()

print("Dequeued:", cq.dequeue())
print("Dequeued:", cq.dequeue())
cq.display()

cq.enqueue(60)
cq.enqueue(70)
cq.display()

print("Front element:", cq.peek())