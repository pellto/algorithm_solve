# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        out = ""
        tmp = self
        while tmp:
            out += str(tmp.val)
            tmp = tmp.next
        return out


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while tmp:
            _next = tmp.next
            if not _next:
                return head
            if tmp.val == _next.val:
                tmp.next = _next.next
            else:
                tmp = _next

        return head


if __name__ == "__main__":
    p1 = ListNode(1, ListNode(1, ListNode(2)))
    p2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    s = Solution()
    print(s.deleteDuplicates(p1))  # [1, 2]
    print(s.deleteDuplicates(p2))  # [1, 2, 3]
