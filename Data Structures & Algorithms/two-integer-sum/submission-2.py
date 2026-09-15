class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            r = target - num

            if r in seen:
                return [seen[r],i]
            else:
                seen[num] = i
            
        return []