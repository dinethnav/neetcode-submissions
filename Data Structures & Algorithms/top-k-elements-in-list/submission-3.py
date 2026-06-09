class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        oc_map = {}
        for i in nums:
            if i in oc_map:
                oc_map[i] +=1
            else:
                oc_map[i] = 1

        freq_map = {}

        for i in oc_map:
            freq = oc_map[i]

            if freq in freq_map:
                freq_map[freq].append(i)

            else:
                freq_map[freq] = [i]

        freqs = sorted(list(freq_map.keys()),reverse = True)
        answer = []
        for i in freqs:
            answer.extend(freq_map[i])

        return answer[:k]
        