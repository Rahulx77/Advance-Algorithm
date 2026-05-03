class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def IsFull(self):
        return len(self.stack) == self.capacity

    def IsEmpty(self):
        return len(self.stack) == 0

    def Push(self, item):
        if self.IsFull():
            print("Stack is full! Cannot push:", item)
        else:
            self.stack.append(item)
            print(f"Pushed: {item}")

    def Pop(self):
        if self.IsEmpty():
            print("Stack is empty! Nothing to pop.")
            return None
        item = self.stack.pop()
        print(f"Popped: {item}")
        return item

    def Peek(self):
        if self.IsEmpty():
            print("Stack is empty! Nothing to peek.")
            return None
        print(f"Top element: {self.stack[-1]}")
        return self.stack[-1]


# --- Quick Test ---
s = Stack(5)
s.Push(10)
s.Push(20)
s.Push(30)
s.Peek()
s.Pop()
s.Peek()
s.Pop()
s.Pop()
s.Pop()   # empty case