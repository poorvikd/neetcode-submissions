class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_n = len(word)
        rows,cols = len(board),len(board[0])
        visited = set()
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(x,y, word_idx):
            # print(x,y,word[word_idx])
            visited.add((x,y))
            word_idx += 1
            if word_idx == word_n:
                return True
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if nx >= 0 and nx < rows and ny >= 0 and ny < cols and (nx,ny) not in visited and word[word_idx] == board[nx][ny]:
                    res = dfs(nx,ny, word_idx)
                    if res:
                        return res
            visited.remove((x,y))
            word_idx -= 1
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    res = dfs(i,j,0)
                    # print(res)
                    if res:
                        return True
        
        return False