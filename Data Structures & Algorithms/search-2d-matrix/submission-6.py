class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        tr,br = 0,r-1
        while br >= tr:
            midr = (br+tr)//2
            if target > matrix[midr][-1]:
                tr = midr + 1
            elif target < matrix[midr][0]:
                br = midr - 1
            else:
                arr = matrix[midr]
                l,r = 0,c-1
                while l<=r:
                    mid = (l+r)//2
                    if target > arr[mid]:
                        l = mid+1
                    elif target < arr[mid]:
                        r = mid-1
                    else:
                        return True
                return False
        return False