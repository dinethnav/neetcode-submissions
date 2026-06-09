class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def climb(i):
            if i == n:
                return 1

            if i > n :
                return 0

            if i in mem:
                return mem[i]

            mem[i] = climb(i+1) + climb(i+2)
            return mem[i]

        return climb(0)

