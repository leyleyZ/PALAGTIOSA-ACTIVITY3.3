
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    """Binary Tree for PALAGTIOSA."""
    root = TreeNode("P")
    root.left, root.right = TreeNode("A"), TreeNode("L")
    root.left.left, root.left.right = TreeNode("A"), TreeNode("G")
    root.right.left, root.right.right = TreeNode("T"), TreeNode("I")
    root.left.left.left = TreeNode("O")
    root.left.left.right = TreeNode("S")
    root.left.right.left = TreeNode("A")

    return root


def tree_bfs(root):
    """Level-Order Traversal (BFS)."""
    order = []

    if root is None:
        return order

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        order.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return order


def tree_dfs(node, order=None):
    """Preorder Traversal (DFS)."""
    if order is None:
        order = []

    if node is None:
        return order

    order.append(node.value)

    tree_dfs(node.left, order)
    tree_dfs(node.right, order)

    return order


if __name__ == "__main__":
    root = build_tree()

    print("=== PALAGTIOSA: Binary Tree ===")
    print("BFS (level-order):", " -> ".join(tree_bfs(root)))
    print("DFS (preorder):   ", " -> ".join(tree_dfs(root)))
