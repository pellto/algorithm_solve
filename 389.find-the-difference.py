class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter, t_counter = dict(), dict()
        for c in s:
            s_counter[c] = s_counter.get(c, 0) + 1
        for c in t:
            t_counter[c] = t_counter.get(c, 0) + 1
        for c in t_counter:
            if c not in s_counter or s_counter[c] != t_counter[c]:
                return c
        return ""


if __name__ == "__main__":
    s = Solution()
    print(s.findTheDifference("abcd", "abcde"))  # e
    print(s.findTheDifference("", "y"))  # y
