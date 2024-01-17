class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        visited = set()   #(row, col)
        row = len(grid)
        col = len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                rCur, cCur = q.pop()
                #down, up, right, left
                direc = [[1,0], [-1,0], [0,1], [0,-1]]

                for rM, cM in direc:
                    changeR = rCur + rM
                    changeC = cCur + cM

                    if (changeR, changeC) not in visited and changeR >= 0 and changeR < row and changeC >= 0 and changeC < col and grid[changeR][changeC] == "1":
                        visited.add((changeR, changeC))
                        q.append((changeR, changeC))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands