class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        j = 0
        i = 0
        subs = ""
        for i in range(len(s)):
            while j<len(t):
                if s[i] == t[j]:
                    subs += s[i]
                    j+=1
                    break
                j+=1

        return s==subs
            

        