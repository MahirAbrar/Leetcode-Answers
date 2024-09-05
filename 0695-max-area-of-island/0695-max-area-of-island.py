class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() #(r,c)


        def dfs(r,c): #return integer
            #base case
            if r < 0 or c < 0 or r == ROWS or c == COLS or ((r,c) in visited or grid[r][c] == 0
            ):
                return 0
            #recursive case
            visited.add((r,c))
            res = 1 + dfs(r+1,c) + dfs(r-1, c) + dfs(r, c+ 1) + dfs(r, c-1)
            
            return res

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))

        return area