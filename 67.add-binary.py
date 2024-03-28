class Solution:
    def addBinary(self, a: str, b: str) -> str:
        _sum = int(a, 2) + int(b, 2)
        return bin(_sum)[2:]


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))  # 100
    print(s.addBinary("1010", "1011"))  # 10101
