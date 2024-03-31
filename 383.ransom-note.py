class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1, counter2 = dict(), dict()
        for c in ransomNote:
            counter1[c] = counter1.get(c, 0) + 1
        for c in magazine:
            counter2[c] = counter2.get(c, 0) + 1
        for c in counter1:
            if c not in counter2 or counter1[c] > counter2[c]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("a", "b"))  # False
    print(s.canConstruct("aa", "ab"))  # False
    print(s.canConstruct("aa", "aab"))  # True
    print(s.canConstruct("aab", "baa"))  # True
    print(s.canConstruct("aba", "baa"))  # True
