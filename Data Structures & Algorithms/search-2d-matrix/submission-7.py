class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top,bottom = 0,m-1
        right_col = n-1
        while top <= bottom:
            mid = (bottom+top)//2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][right_col] < target:
                top = mid + 1
            else:
                l,r = 0,n-1
                while l<=r:
                    mid_col = (l+r)//2
                    if matrix[mid][mid_col] > target:
                        r = mid_col - 1
                    elif matrix[mid][mid_col] < target:
                        l = mid_col + 1
                    else:
                        return True
                return False
        
        return False
