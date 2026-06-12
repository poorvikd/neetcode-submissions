class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        email_db = {}
        def find(n1):
            if n1 != parent[n1]:
                parent[n1] = find(parent[n1])
            return parent[n1]

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p1]>=rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
        
        for i,acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_db:
                    union(i, email_db[email])
                else:
                    email_db[email] = i
                    
        groups = defaultdict(list)
        for email,i in email_db.items():
            res = i
            while res != parent[res]:
                res = parent[res]
            groups[res].append(email)

        res = []
        for i,emails in groups.items():
            res.append([accounts[i][0]]+sorted(emails))

        return res