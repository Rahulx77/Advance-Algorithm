class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1

    def push_rear(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        self.size -= 1
        return data

    def pop_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
        self.size -= 1
        return data

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.data

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.data

    def __len__(self):
        return self.size

    def __repr__(self):
        result, curr = [], self.front
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        return "Deque([" + " <-> ".join(result) + "])"


# Usage
dq = Deque()
dq.push_rear(10)
dq.push_rear(20)
dq.push_front(5)
dq.push_front(1)

print(dq)             # Deque([1 <-> 5 <-> 10 <-> 20])
print(dq.pop_front()) # 1
print(dq.pop_rear())  # 20
print(dq.peek_front())# 5
print(len(dq))        # 2