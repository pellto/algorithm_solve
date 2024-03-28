# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )


if __name__ == "__main__":
    s = Solution()
    h1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    h2 = TreeNode()
    h3 = TreeNode(1)
    print(s.inorderTraversal(h1))  # [1,3,2]
    print(s.inorderTraversal(h2))  # []
    print(s.inorderTraversal(h3))  # [1]
