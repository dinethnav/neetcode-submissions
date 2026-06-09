class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        
        prev = nums[0]

        curr_length = 1
        max_length = 0

        for i in range(1,len(nums)):
            if prev +1 == nums[i]:
                curr_length+=1
                prev = nums[i]

            else:
                max_length = max(curr_length,max_length)
                curr_length = 1
                prev = nums[i]

        max_length = max(curr_length,max_length)

        return max_length
        