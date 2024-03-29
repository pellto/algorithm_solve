# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = self.traversal(root, 0)
        return level

    def traversal(self, root: Optional[TreeNode], level: int) -> int:
        if not root:
            return level
        return (
            max(
                self.traversal(root.left, level),
                self.traversal(root.right, level),
            )
            + 1
        )


if __name__ == "__main__":
    s = Solution()
    p1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    p2 = TreeNode(1, None, TreeNode(2))
    print(s.maxDepth(p1))  # 3
    print(s.maxDepth(p2))  # 2
