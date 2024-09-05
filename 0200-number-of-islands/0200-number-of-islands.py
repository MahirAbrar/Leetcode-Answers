class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        visited = set()
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

 

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r >= 0 and r < ROWS and c >= 0 and c < COLS and (r,c) not in visited and grid[r][c] == "1":
                        q.append((r,c))
                        visited.add((r,c))
                        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands 