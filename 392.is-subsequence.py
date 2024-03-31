class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        s_idx, t_idx = 0, 0
        while t_idx < len(t) and s_idx < len(s):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        return s_idx == len(s)


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))  # True
    print(s.isSubsequence("axc", "ahbgdc"))  # False
