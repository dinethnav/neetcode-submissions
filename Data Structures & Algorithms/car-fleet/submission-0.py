class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        q = collections.deque()

        pos_time = []
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            pos_time.append((position[i],time))

        pos_time = sorted(pos_time)

        for i in range(-1,-len(pos_time)-1,-1):
            if not q:
                q.append(pos_time[i])

            else:
                if pos_time[i][1] > q[-1][1]:
                    q.append(pos_time[i])

        return len(q)
        