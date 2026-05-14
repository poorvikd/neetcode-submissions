class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        m,n = len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        visited = [[0]*n for i in range(m)]
        
        while len(queue) != 0:
            x,y,dist = queue.pop()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if grid[nx][ny] == -1 or (visited[nx][ny] == 1 and grid[nx][ny] < dist+1):
                    continue
                visited[nx][ny] = 1
                grid[nx][ny] = min(grid[nx][ny], dist+1)
                queue.append((nx,ny,dist+1))
        
        return
