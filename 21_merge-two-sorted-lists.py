from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        tmp = self
        out = "["
        while tmp:
            out += f"{tmp.val}, "
            tmp = tmp.next
        return out + "\b\b]"


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = start = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2

        if list1 or list2:
            current.next = list1 if list1 else list2

        return start.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    l2.next = ListNode(4)
    ll1 = ListNode(1)
    ll2 = ListNode(3)
    ll1.next = ll2
    ll2.next = ListNode(4)
    s = Solution()
    print(l1)
    print(ll1)
    print(s.mergeTwoLists(l1, ll1))  # [1, 1, 2, 3, 4, 4]
