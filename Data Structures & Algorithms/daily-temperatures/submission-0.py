class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = collections.deque()

        answer = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            if not q:
                q.append((temperatures[i],i))
            else:
                while q and temperatures[i] > q[-1][0]:
                    top = q.pop()
                    top_index= top[1]
                    top_distance = i - top_index

                    answer[top_index] = top_distance

                q.append((temperatures[i],i))


        return answer
        