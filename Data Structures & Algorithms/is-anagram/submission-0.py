class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        def enter_val(hmap, val):
            try: 
                hmap[val] +=1
            except:
                hmap[val] = 1
        for i in range(len(s)):
            enter_val(s_dict,s[i])
            enter_val(t_dict,t[i])

        return s_dict == t_dict 
            
        