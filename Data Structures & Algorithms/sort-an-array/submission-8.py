class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ## Insertion Sort
        # for i in range(1,len(nums)):
        #     j = i-1
        #     while j>=0 and nums[j]>nums[j+1]:
        #         nums[j],nums[j+1] = nums[j+1],nums[j]
        #         j -= 1
        
        ## Selection Sort
        # for i in range(n):
        #     mn = nums[i]
        #     mn_i = i
        #     for j in range(i+1,n):
        #         if mn>nums[j]:
        #             mn_i = j
        #             mn = nums[j]
        #     nums[i],nums[mn_i] = nums[mn_i],nums[i]

        ## Bubble Sort
        # for i in range(n):
        #     for j in range(0,n-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]

        ## Merge Sort

        # def merge_sort(nums):
        #     n = len(nums)
        #     if n <= 1:
        #         return nums
        #     mid = n//2
        #     left = merge_sort(nums[:mid])
        #     right = merge_sort(nums[mid:])
        #     return merge(left, right)
        
        # def merge(left, right):
        #     res = []
        #     i = 0
        #     j = 0

        #     while i<len(left) and j<len(right):
        #         if left[i]>right[j]:
        #             res.append(right[j])
        #             j += 1
        #         elif left[i] < right[j]:
        #             res.append(left[i])
        #             i += 1
        #         else:
        #             res.append(left[i])
        #             res.append(right[j])
        #             i += 1
        #             j += 1
        #     while i<len(left):
        #         res.append(left[i])
        #         i += 1
        #     while j<len(right):
        #         res.append(right[j])
        #         j += 1
        #     return res
        
        # return merge_sort(nums)

        ## Quick Sort

        def quick_sort(l,r):
            import random
            if l >= r:
                return

            rand_idx = random.randint(l, r)
            nums[rand_idx], nums[r] = nums[r], nums[rand_idx]
            pivot = nums[r]
            i = l-1
            j = l
            while j<r:
                if nums[j] < pivot:
                    i += 1
                    nums[i],nums[j] = nums[j],nums[i]
                j += 1
            nums[i+1],nums[r] = nums[r], nums[i+1]
            pivot_idx = i + 1
            quick_sort(l, pivot_idx - 1)
            quick_sort(pivot_idx + 1, r)

        quick_sort(0,len(nums)-1)
        return nums
                