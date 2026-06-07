class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        heapq.heapify(tasks)
        priority_q = []
        heapq.heapify(priority_q)
        time = 0
        curr_task = None
        res = []
        while tasks or priority_q:
            if curr_task and time == curr_task[2]+curr_task[0]:
                curr_task = None
            
            while tasks and time >= tasks[0][0]:
                top = heapq.heappop(tasks)
                job = [top[1],top[2]]
                heapq.heappush(priority_q, job)
            
            if curr_task == None and len(priority_q)>0:
                curr_task = heapq.heappop(priority_q)
                curr_task.append(time)
                res.append(curr_task[1])
                time += curr_task[0] - 1
            elif tasks:
                time = tasks[0][0] - 1
            time += 1
        
        return res
