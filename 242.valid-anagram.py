class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = dict()
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        for c in t:
            if c not in counter:
                return False
            counter[c] -= 1
        for key in counter:
            if counter[key] != 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))  # True
    print(s.isAnagram("cat", "rat"))  # False
