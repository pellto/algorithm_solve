class Solution:
    def sumZero(self, n):
        ret = []
        if n % 2 != 0:
            ret = [0]

        for i in range(1, 1 + n//2):
            ret += [-i, i]
        return ret


if __name__=="__main__":
    print(Solution().sumZero(5))
    print(Solution().sumZero(3))
    print(Solution().sumZero(1))
