class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subsets = []
        n = len(s)

        def isPalindrome(s):
            n = len(s)
            if n == 1:
                return True
            if n == 2:
                return s[0] == s[1]
            else:
                i = 0
                while i <= n//2:
                    if s[i] != s[n-i-1]:
                        return False
                    i += 1
            return True
        def dfs(idx, subset):

            if idx == n:
                subsets.append(subset.copy())
                return
            for i in range(idx,n):
                s1 = s[idx:i+1]
                # print(s1)
                if not isPalindrome(s1):
                    continue
                subset.append(s1)
                dfs(i+1,subset)
                subset.pop(-1)
    
        # print(isPalindrome("A"))
        # print(isPalindrome("AB"))
        # print(isPalindrome("AA"))
        # print(isPalindrome("ACA"))
        dfs(0,[])
        return subsets
