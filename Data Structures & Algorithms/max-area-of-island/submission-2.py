class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        visited = [[0]*m for i in range(n)]
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(x,y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return 0
            if grid[x][y] == 0 or visited[x][y] == 1:
                return 0
            visited[x][y] = 1
            area = 0
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                area += dfs(nx,ny)
            return 1+area
        max_area = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    print(f"starting {r},{c}")
                    area = dfs(r,c)
                    max_area = max(area, max_area)
        return max_area