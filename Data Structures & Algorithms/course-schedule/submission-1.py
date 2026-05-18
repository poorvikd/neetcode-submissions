class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indeg = defaultdict(lambda: 0)
        outdeg = defaultdict(lambda: 0)
        adj = defaultdict(list)
        for a,b in prerequisites:
            indeg[a] += 1
            outdeg[b] += 1
            adj[b].append(a)

        # print(adj)
        visited = [0 for i in range(numCourses)]
        inStack = [0 for i in range(numCourses)]
        def dfs(node):
            # print(visited)
            # print(inStack)
            if visited[node] == 1 and inStack[node] == 1:
                # print(f"Already visited {node} which is in Stack")
                return False
            elif visited[node] == 1  and inStack[node] == 0:
                # print(f"Already visited {node} which is not in Stack")
                return True

            inStack[node] = 1
            visited[node] = 1
            resp = True
            for neighbor in adj[node]:
                # print(f"visited {neighbor}")
                resp &= dfs(neighbor)
            
            inStack[node] = 0
            return resp
        
        for i in range(numCourses):
            if visited[i] == 0:
                hasCycle = dfs(i)
                if hasCycle == False:
                    return False
        
        return True
