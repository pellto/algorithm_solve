class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        f0, f1 = 0, 1
        out = 0
        for _ in range(n - 1):
            out = f0 + f1
            f0, f1 = f1, out
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.fib(2))  # 1
    print(s.fib(3))  # 2
    print(s.fib(4))  # 3
