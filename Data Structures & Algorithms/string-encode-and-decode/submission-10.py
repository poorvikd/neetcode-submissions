class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            if len(s) == 0:
                st+="\\,"
                continue
            for c in s:
                st+= str(ord(c)) + ':'
            st += ','
        return st

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        words = s.strip(',').split(',')
        res = []
        for word in words:
            if word=='\\':
                res.append("")
                continue
            word = word.strip(':').split(':')
            c = [chr(int(i)) for i in word]
            res.append("".join(c))

        return res
