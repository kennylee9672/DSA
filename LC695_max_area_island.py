'''
https://leetcode.com/problems/max-area-of-island/description/

695. Max Area of Island
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(r, c):
            nonlocal count
            if (r not in range(m) or c not in range(n) or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            return (
                1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
            )

        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = max(count, dfs(i, j))
        return count
