class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}

        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        for i in t:
            if i in counter:
                counter[i] -= 1
            else:
                return False

        for i in counter:
            if counter[i] != 0:
                return False
        
        return True