class Solution:
    def isValid(self, s: str) -> bool:
        q = collections.deque()

        open_b = set(["{" , "(" , "["])

        close_b = {"}":"{" ,
                ")" : "(", 
                "]" : "["}

        for i in s:
            if i in open_b:
                q.append(i)
            
            else:
                if q and q[-1] == close_b[i]:
                    q.pop()
                else:
                    return False
                
        if q :
            return False
        else: 
            return True
        