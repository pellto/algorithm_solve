class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num
        while left <= right:
            middle = (left + right) // 2
            _pow = middle * middle
            if _pow < num:
                left = middle + 1
            elif _pow > num:
                right = middle - 1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(16))  # True
    print(s.isPerfectSquare(14))  # False
    print(s.isPerfectSquare(104976))  # True
