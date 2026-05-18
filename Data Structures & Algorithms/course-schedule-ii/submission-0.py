class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = defaultdict(lambda: 0)
        outdeg = defaultdict(lambda: 0)
        adj = defaultdict(list)
        for a,b in prerequisites:
            indeg[a] += 1
            outdeg[b] += 1
            adj[b].append(a)

        visited = [0 for i in range(numCourses)]
        inStack = [0 for i in range(numCourses)]
        def dfs(node):
            if visited[node] == 1 and inStack[node] == 1:
                return False
            elif visited[node] == 1  and inStack[node] == 0:
                return True

            inStack[node] = 1
            visited[node] = 1
            resp = True
            for neighbor in adj[node]:
                resp &= dfs(neighbor)
            
            inStack[node] = 0
            return resp
        queue = deque()
        for i in range(numCourses):
            if visited[i] == 0:
                hasCycle = dfs(i)
                if hasCycle == False:
                    return []
            if indeg[i] == 0:
                queue.append((i,0))
        
        output = []
        # visited = [0 for i in range(numCourses)]
        while queue:
            node, level = queue.pop()
            output.append(node)
            for neighbor in adj[node]:
                queue.append((neighbor,level+1))
        
        return output