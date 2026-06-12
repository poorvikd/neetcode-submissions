class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l,r = 0,n-1
        pos = -1
        while l<=r:
            mid = (l+r)//2
            if arr[mid] > x:
                r = mid - 1
            elif arr[mid] < x:
                pos = max(mid, pos) 
                l = mid + 1
            else:
                pos = mid
                break
        
        def closest(a,b):
            num1,num2 = arr[a],arr[b]
            if abs(num1-x) < abs(num2-x):
                return a
            elif abs(num1-x) > abs(num2-x):
                return b
            else:
                if num1>num2:
                    return b
                else:
                    return a
        
        if pos != n-1:
            pos = closest(pos,pos+1)
        window = deque()
        window.appendleft(arr[pos])
        count = 1
        l,r = pos,pos
        while count < k and 0<=l<=r and r<n:
            optionA = l-1
            optionB = r+1
            if optionA >= 0 and optionB <= n-1:
                pos = closest(optionA,optionB)
            elif optionA < 0:
                pos = optionB
            else:
                pos = optionA
            
            # print(pos)
            if pos == optionA:
                window.appendleft(arr[pos])
                l = pos
            else:
                window.append(arr[pos])
                r = pos
            # print(window)
            count += 1

        return list(window)
        