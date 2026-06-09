class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <2:
            return len(s)

        sub = set([s[0]])

        l = 0 
        r = 1

        max_len = 1

        while r<len(s):
            char = s[r]

            if char not in sub:
                sub.add(char)
                max_len = max(max_len,(r-l+1))
                r+=1

            else:
                while s[l] != char:
                    sub.discard(s[l])
                    l+=1
                l+=1 
                r+=1

        return max_len