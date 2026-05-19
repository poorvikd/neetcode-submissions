class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum = [[0]*(cols+1) for i in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                self.prefixSum[i+1][j+1] = matrix[i][j] + self.prefixSum[i+1][j] + self.prefixSum[i][j+1] - self.prefixSum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        nr1,nr2,nc1,nc2 = row1+1,row2+1,col1+1,col2+1
        return self.prefixSum[nr2][nc2] - self.prefixSum[nr1-1][nc2] - self.prefixSum[nr2][nc1-1] + self.prefixSum[nr1-1][nc1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)