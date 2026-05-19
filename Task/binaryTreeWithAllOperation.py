"""
Binary Tree Implementation
==========================
Covers:
  1. Simple Binary Tree
  2. Breadth-First Search (BFS)
  3. InOrder, PreOrder, PostOrder Traversal
  4. Insertion and Deletion
     - Deletion replaces the target node's value with the
       bottom-most, rightmost node's value, then removes
       that leaf (tree shrinks from the bottom).
"""

from collections import deque


# ─────────────────────────────────────────────
# 1. Node & Binary Tree
# ─────────────────────────────────────────────

class Node:
    """A single node in the binary tree."""
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


class BinaryTree:
    """
    Simple Binary Tree that stores nodes level-by-level
    (insertion always fills the next available spot via BFS order).
    """

    def __init__(self):
        self.root = None

    # ─────────────────────────────────────────
    # 4a. Insertion
    # ─────────────────────────────────────────
    def insert(self, data):
        """
        Insert a new node at the first available position
        in level-order (BFS order), keeping the tree complete.
        """
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    # ─────────────────────────────────────────
    # 2. Breadth-First Search (BFS)
    # ─────────────────────────────────────────
    def bfs(self):
        """
        Level-order traversal using a queue.
        Returns a list of node values visited in BFS order.
        """
        if self.root is None:
            return []

        result = []
        queue  = deque([self.root])

        while queue:
            current = queue.popleft()
            result.append(current.data)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    # ─────────────────────────────────────────
    # 3a. InOrder  (Left → Root → Right)
    # ─────────────────────────────────────────
    def inorder(self, node=None, _first_call=True):
        """InOrder traversal: Left → Root → Right."""
        if _first_call:
            node = self.root
        if node is None:
            return []
        return (self.inorder(node.left,  _first_call=False) +
                [node.data] +
                self.inorder(node.right, _first_call=False))

    # ─────────────────────────────────────────
    # 3b. PreOrder  (Root → Left → Right)
    # ─────────────────────────────────────────
    def preorder(self, node=None, _first_call=True):
        """PreOrder traversal: Root → Left → Right."""
        if _first_call:
            node = self.root
        if node is None:
            return []
        return ([node.data] +
                self.preorder(node.left,  _first_call=False) +
                self.preorder(node.right, _first_call=False))

    # ─────────────────────────────────────────
    # 3c. PostOrder (Left → Right → Root)
    # ─────────────────────────────────────────
    def postorder(self, node=None, _first_call=True):
        """PostOrder traversal: Left → Right → Root."""
        if _first_call:
            node = self.root
        if node is None:
            return []
        return (self.postorder(node.left,  _first_call=False) +
                self.postorder(node.right, _first_call=False) +
                [node.data])

    # ─────────────────────────────────────────
    # 4b. Deletion
    # ─────────────────────────────────────────
    def _get_deepest_rightmost(self):
        """
        BFS to find:
          - the node whose value should replace the target  (deepest-rightmost node)
          - its parent (so we can unlink it)
        Returns (deepest_node, parent_of_deepest).
        """
        if self.root is None:
            return None, None

        queue  = deque([self.root])
        last   = None
        parent = None

        while queue:
            current = queue.popleft()
            last = current

            if current.left:
                parent = current
                queue.append(current.left)
            if current.right:
                parent = current
                queue.append(current.right)

        return last, parent

    def _delete_deepest(self, deepest_node, parent):
        """Remove the deepest-rightmost node from the tree."""
        if parent is None:
            # deepest_node IS the root → tree becomes empty
            self.root = None
            return

        if parent.right is deepest_node:
            parent.right = None
        elif parent.left is deepest_node:
            parent.left = None

    def delete(self, data):
        """
        Delete the node containing *data*.
        Strategy:
          1. Find the target node via BFS.
          2. Find the deepest-rightmost node (and its parent).
          3. Copy deepest-rightmost value into the target node.
          4. Delete the deepest-rightmost leaf.
        The tree therefore always shrinks from the bottom.
        """
        if self.root is None:
            print(f"Tree is empty. Cannot delete {data}.")
            return

        # ── Step 1: find target node via BFS ──────────────────
        target_node = None
        queue = deque([self.root])

        while queue:
            current = queue.popleft()
            if current.data == data:
                target_node = current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        if target_node is None:
            print(f"Value {data} not found in tree.")
            return

        # ── Step 2 & 3: get deepest-rightmost and copy its value ──
        deepest_node, parent = self._get_deepest_rightmost()
        target_node.data = deepest_node.data   # replace target's value

        # ── Step 4: delete the deepest-rightmost leaf ─────────
        self._delete_deepest(deepest_node, parent)
        print(f"Deleted {data}. Tree shrunk from the bottom-most rightmost node.")

    # ─────────────────────────────────────────
    # Pretty-print helper
    # ─────────────────────────────────────────
    def display(self):
        """Print the tree level by level."""
        if self.root is None:
            print("(empty tree)")
            return

        queue  = deque([(self.root, 0)])
        level  = 0
        line   = []

        while queue:
            node, lv = queue.popleft()
            if lv != level:
                print(f"  Level {level}: {line}")
                line  = []
                level = lv
            line.append(node.data)
            if node.left:
                queue.append((node.left,  lv + 1))
            if node.right:
                queue.append((node.right, lv + 1))

        print(f"  Level {level}: {line}")


# ─────────────────────────────────────────────
# Demo / Driver
# ─────────────────────────────────────────────

if __name__ == "__main__":
    separator = "─" * 50

    print(separator)
    print("  1. Building Binary Tree")
    print(separator)
    bt = BinaryTree()
    for value in [1, 2, 3, 4, 5, 6, 7]:
        bt.insert(value)

    print("Tree (level-by-level):")
    bt.display()
    #
    #          1
    #        /   \
    #       2     3
    #      / \   / \
    #     4   5 6   7

    print()
    print(separator)
    print("  2. Breadth-First Search (BFS)")
    print(separator)
    print(f"  BFS order: {bt.bfs()}")

    print()
    print(separator)
    print("  3. DFS Traversals")
    print(separator)
    print(f"  InOrder   (L→Root→R): {bt.inorder()}")
    print(f"  PreOrder  (Root→L→R): {bt.preorder()}")
    print(f"  PostOrder (L→R→Root): {bt.postorder()}")

    print()
    print(separator)
    print("  4a. Insertion — adding node 8")
    print(separator)
    bt.insert(8)
    bt.display()

    print()
    print(separator)
    print("  4b. Deletion — deleting node with value 3")
    print("      (replaced by bottom-most rightmost node)")
    print(separator)
    bt.delete(3)
    print("\nTree after deletion:")
    bt.display()
    print(f"\n  BFS after deletion: {bt.bfs()}")
    print(f"  InOrder   after deletion: {bt.inorder()}")

    print()
    print(separator)
    print("  Edge case: deleting root (1)")
    print(separator)
    bt.delete(1)
    print("Tree after deleting root:")
    bt.display()

    print()
    print(separator)
    print("  Edge case: deleting non-existent value (99)")
    print(separator)
    bt.delete(99)

    print()
    print(separator)
    print("  Edge case: single-node tree, delete root")
    print(separator)
    single = BinaryTree()
    single.insert(42)
    print("Before:")
    single.display()
    single.delete(42)
    print("After:")
    single.display()