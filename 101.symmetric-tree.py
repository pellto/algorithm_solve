# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.leftFirstTraversal(root.left)
        right = self.rightFirstTraversal(root.right)

        print("left >> ", left)
        print("right >> ", right)

        if len(left) != len(right):
            return False

        for l, r in zip(left, right):
            if l != r:
                return False
        return True

    def leftFirstTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [1001]
        return (
            [root.val]
            + self.leftFirstTraversal(root.left)
            + self.leftFirstTraversal(root.right)
        )

    def rightFirstTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [1001]
        return (
            [root.val]
            + self.rightFirstTraversal(root.right)
            + self.rightFirstTraversal(root.left)
        )


if __name__ == "__main__":
    s = Solution()
    p1 = TreeNode(
        1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3)),
    )
    p2 = TreeNode(
        1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))
    )
    print(s.isSymmetric(p1))  # True
    print(s.isSymmetric(p2))  # False
