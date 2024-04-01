from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # N W E S
        y = perimeter = 0
        while y < len(grid):
            x = 0
            while x < len(grid[0]):
                if grid[y][x] == 1:
                    perimeter += 4
                    for direction in directions:
                        n_y, n_x = y + direction[0], x + direction[1]
                        if (
                            0 <= n_y < len(grid)
                            and 0 <= n_x < len(grid[0])
                            and grid[n_y][n_x] == 1
                        ):
                            perimeter -= 1
                x += 1
            y += 1
        return perimeter


if __name__ == "__main__":
    s = Solution()
    print(
        s.islandPerimeter(
            [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        )
    )  # 16
    print(s.islandPerimeter([[1]]))  # 4
    print(s.islandPerimeter([[1, 0]]))  # 4
    print(s.islandPerimeter([[1, 1]]))  # 6
