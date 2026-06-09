class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpn = [char.lower() for char in s if char.isalnum()]
        start = 0 
        end = len(alpn)-1

        while start<end:
            if alpn[start] != alpn[end]:
                return False
            
            start+=1
            end-=1

        return True
        