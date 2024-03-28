# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_travasal = self.inorderTraversal(p)
        q_travasal = self.inorderTraversal(q)
        # print("p_travasal >> ", p_travasal)
        # print("q_travasal >> ", q_travasal)
        if len(p_travasal) != len(q_travasal):
            return False
        for pv, qv in zip(p_travasal, q_travasal):
            if pv != qv:
                return False
        return True

    def inorderTraversal(self, p: Optional[TreeNode]) -> List[int]:
        if not p:
            return [10**4 + 1]
        return (
            [p.val]
            + self.inorderTraversal(p.left)
            + self.inorderTraversal(p.right)
        )


if __name__ == "__main__":
    s = Solution()
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    print("problem 1 >> ", s.isSameTree(p1, q1))  # True
    print("problem 2 >> ", s.isSameTree(p2, q2))  # False
    print("problem 3 >> ", s.isSameTree(p3, q3))  # False
    p4 = TreeNode(1, TreeNode(1), None)
    q4 = TreeNode(1, None, TreeNode(1))
    print("problem 4 >> ", s.isSameTree(p4, q4))  # False
