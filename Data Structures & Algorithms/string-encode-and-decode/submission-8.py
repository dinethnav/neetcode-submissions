class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            for c in s:
                res.append(str(ord(c)))
                res.append("-2")
            res.append("-1")
        
        return "".join(res)
            

    def decode(self, s: str) -> List[str]:
        arr = s.split("-1")
        arr.pop()
        print(arr)
        res = []
        for s in arr:
            tmp = []
            cs = s.split("-2")
            cs.pop()
            print(cs)
            for c in cs:
                tmp.append(chr(int(c)))
            res.append("".join(tmp))

        return res
