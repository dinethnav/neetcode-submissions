class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = []

        for s in strs:
            encoding.append(str(len(s)))
            encoding.append(",")
        encoding.append("#")
        encoding.extend(strs)

        return "".join(encoding)


    def decode(self, s: str) -> List[str]:
        i = 0
        while s[i] != "#":
            i+=1

        decoded = s[i+1:]
        lengths = s[:i].split(",")
        lengths.pop()

        res = []
        i = 0
        for l in lengths:
            res.append(decoded[i:i+int(l)])
            i = i + int(l)
        
        return res

