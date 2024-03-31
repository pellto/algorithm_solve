BAD_VERSION = -1


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            middle_version = (left + right) // 2
            if isBadVersion(middle_version):
                right = middle_version - 1
            else:
                left = middle_version + 1
        return left


if __name__ == "__main__":
    s = Solution()
    BAD_VERSION = 4
    print(s.firstBadVersion(5))  # 4
    BAD_VERSION = 1
    print(s.firstBadVersion(1))  # 1
