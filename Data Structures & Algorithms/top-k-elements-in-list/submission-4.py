class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        arr = []

        for item in counter:
            arr.append([counter[item],item])
        
        arr.sort()

        res = []

        for i in range(k):
            res.append(arr.pop()[1])

        return res

        