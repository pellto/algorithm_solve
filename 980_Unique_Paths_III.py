class Solution:
    """
    Runtime: 52 ms, faster than 88.50%
    Memory Usage: 14.2 MB, less than 73.49%
    """
    def uniquePathsIII(self, grid):
        def dfs(y, x, remain):
            if grid[y][x] == 2:
                if remain == 0:
                    self.answer += 1
                return

            grid[y][x] = -1
            for yy, xx in [[y, x + 1], [y + 1, x], [y, x - 1], [y - 1, x]]:
                if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]) and grid[yy][xx] in (0, 2):
                    dfs(yy, xx, remain - 1)
            grid[y][x] = 0

        self.answer, remain = 0, 0
        start_x, start_y = -1, -1
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] in (0, 1):
                    remain += 1
                    if grid[y][x] == 1:
                        start_y, start_x = y, x

        dfs(start_y, start_x, remain)
        return self.answer
