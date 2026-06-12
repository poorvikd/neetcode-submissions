class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i:i for i in range(1,n+1)}
        rank = {i:1 for i in range(1,n+1)}

        def find(n1):
            if n1 != parent[n1]:
                parent[n1] = find(parent[n1])
            return parent[n1]
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if p1 == p2:
                return True
            
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return False
        
        for s,d in edges:
            res = union(s,d)
            if res:
                return [s,d]
                
