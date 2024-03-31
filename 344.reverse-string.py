from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]


if __name__ == "__main__":
    s = Solution()
    p1 = ["h", "e", "l", "l", "o"]
    p2 = ["H", "a", "n", "n", "a", "h"]
    p3 = ["a", "b", "c", "d", "e"]
    p4 = ["a", "b"]
    p5 = ["a", "b", "c", "d"]
    s.reverseString(p1)
    print(p1)  # ["o","l","l","e","h"]
    s.reverseString(p2)
    print(p2)  # ["h","a","n","n","a","H"]
    s.reverseString(p3)
    print(p3)  # ["e", "d", "c", "b", "a"]
    s.reverseString(p4)
    print(p4)  # ["b", "a"]
    s.reverseString(p5)
    print(p5)  # ["d", "c", "b", "a"]
