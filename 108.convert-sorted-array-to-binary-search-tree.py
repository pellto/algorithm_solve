# TODO: LATER

# # Definition for a binary tree node.
# from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         start_idx = (len(nums) - 1) // 2
#         is_even = not len(nums) % 2
#         root = TreeNode(nums[start_idx])
#         idx = 1
#         while start_idx - idx <= 0:
#             self.insert(root, nums[start_idx + idx])
#             self.insert(root, nums[start_idx - idx])
#             idx += 1
#         if is_even:
#             self.insert(root, nums[-1])
#         return root

#     def insert(self, root: Optional[TreeNode], val: int):
#         current = root
#         while True:
#             if val < current.val:
#                 if current.left is not None:
#                     current = current.left
#                 else:
#                     current.left = TreeNode(val)
#                     break
#             else:
#                 if current.right is not None:
#                     current = current.right
#                 else:
#                     current.right = TreeNode(val)
#                     break


# if __name__ == "__main__":
#     s = Solution()
#     print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))  # [0,-3,9,-10,null,5]
#     print(s.sortedArrayToBST([1, 3]))  # [3, 1]
#     print(s.sortedArrayToBST([1]))  # [1]
