class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        single_set = set(["0", "1", "8"])
        mapper = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        idx = 0
        while idx < (len(num) // 2):
            if num[idx] not in mapper:
                return False
            if mapper[num[idx]] != num[-1 - idx]:
                return False
            idx += 1
        if len(num) % 2:
            return num[len(num) // 2] in single_set
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isStrobogrammatic("69"))  # True
    print(s.isStrobogrammatic("88"))  # True
    print(s.isStrobogrammatic("962"))  # False
    print(s.isStrobogrammatic("25"))  # False
    print(s.isStrobogrammatic("6"))  # False
    print(s.isStrobogrammatic("1"))  # True
    print(s.isStrobogrammatic("868"))  # False
