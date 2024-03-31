class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = dict()
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        for c in counter:
            if counter[c] == 1:
                return s.index(c)
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))  # 0
    print(s.firstUniqChar("loveleetcode"))  # 2
    print(s.firstUniqChar("aabb"))  # -1
