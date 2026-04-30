class myStack:
    def __init__(self, cap):
        self.arr = []
        self.cap = cap

    def push(self, item):
        if len(self.arr) == self.cap:
            print("Stack is Full")
        else:
            self.arr.append(item)
            print("Pushed:", item)

    def pop(self):
        if len(self.arr) == 0:
            print("Stack is Empty")
        else:
            print("Popped:", self.arr.pop())

    def display(self):
        if len(self.arr) == 0:
            print("Stack is Empty")
        else:
            print("Stack:", self.arr)


# -------- USER INPUT --------
cap = int(input("Enter stack size: "))
s = myStack(cap)

while True:
    print("\n1.Push  2.Pop  3.Display  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        item = int(input("Enter value: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")