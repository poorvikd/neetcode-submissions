class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dist = 0

        work_queue = []
        curr_queue = []
        heapq.heapify(work_queue)
        heapq.heapify(curr_queue)
        curr_cap = 0
        for trip in trips:
            heapq.heappush(work_queue,(trip[1],trip[2],trip[0]))
        
        while work_queue or curr_queue:
            while len(curr_queue) > 0 and dist == curr_queue[0][0]:
                task = heapq.heappop(curr_queue)
                curr_cap -= task[2]
            
            while len(work_queue) > 0 and  dist == work_queue[0][0]:
                task = heapq.heappop(work_queue)
                if curr_cap + task[2] > capacity:
                    return False
                heapq.heappush(curr_queue, (task[1],task[0],task[2]))
                curr_cap += task[2]
            
            dist += 1
        
        return True
            