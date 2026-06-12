class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        num_components = n

        def find(n1):
            if parent[n1] != n1:
                parent[n1] = find(parent[n1])
            return parent[n1]
            
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return 0
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        for s,d in edges:
            num_components -= union(s,d)
                
        
        return num_components
