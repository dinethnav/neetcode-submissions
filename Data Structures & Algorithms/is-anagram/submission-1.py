class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        t_counter = {}
        s_counter = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in s_counter:
                s_counter[s_char] +=1

            elif s_char not in s_counter:
                s_counter[s_char] = 1

            if t_char in t_counter:
                t_counter[t_char] += 1

            elif t_char not in t_counter:
                t_counter[t_char] = 1


        return t_counter == s_counter
        