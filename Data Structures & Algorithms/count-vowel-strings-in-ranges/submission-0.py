class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        ps = [0 for i in range(n+1)]

        def check_vowel(word):
            if word[0] in ['a','e','i','o','u'] and word[-1] in ['a','e','i','o','u']:
                return 1
            return 0
        for i in range(1,n+1):
            ps[i] = ps[i-1] + check_vowel(words[i-1])
        
        res = []
        for q in queries:
            res.append(ps[q[1]+1]-ps[q[0]])
        return res