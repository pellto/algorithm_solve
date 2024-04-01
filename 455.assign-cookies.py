from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie_idx, children_idx = 0, 0
        while cookie_idx < len(s) and children_idx < len(g):
            if g[children_idx] <= s[cookie_idx]:
                children_idx += 1
            cookie_idx += 1
        return children_idx


if __name__ == "__main__":
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 1]))  # 1
    print(s.findContentChildren([1, 2], [1, 2, 3]))  # 2
