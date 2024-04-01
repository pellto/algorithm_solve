from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        candidate = []
        max_sums = -1
        for W in range(1, int(area**0.5) + 1):
            L = area // W
            if L * W != area:
                continue
            if max_sums < L + W:
                candidate = [L, W]
        return candidate


if __name__ == "__main__":
    s = Solution()
    print(s.constructRectangle(4))  # [2, 2]
    print(s.constructRectangle(37))  # [37, 1]
    print(s.constructRectangle(122122))  # [427,286]
