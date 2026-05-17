class ArrayBinaryTree:
    def __init__(self, size):
        self.size = size
        self.tree = [-1] * size

    def insert_root(self, value):
        self.tree[0] = value

    def insert_left(self, parent_index, value):
        left_index = 2 * parent_index + 1
        if left_index < self.size:
            self.tree[left_index] = value

    def insert_right(self, parent_index, value):
        right_index = 2 * parent_index + 2
        if right_index < self.size:
            self.tree[right_index] = value

    def display(self):
        for i in self.tree:
            print(i if i != -1 else "_", end=" ")
        print()


# Example usage
bt = ArrayBinaryTree(10)

bt.insert_root(10)
bt.insert_left(0, 20)
bt.insert_right(0, 30)
bt.insert_left(1, 40)
bt.insert_right(1, 50)

bt.display()