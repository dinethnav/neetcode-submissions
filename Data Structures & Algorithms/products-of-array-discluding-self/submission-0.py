class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = []
        post_prof = []

        for i in nums:
            if len(pref_prod) == 0:
                pref_prod.append(i)
            else:
                pref_prod.append(i*pref_prod[-1])

        for i in range(len(nums) -1 , -1, -1):
            if len(post_prof) == 0:
                post_prof.append(nums[i])

            else:
                post_prof.insert(0,nums[i] * post_prof[0])

        result = []
        for i in range(len(nums)):
            if i ==0:
                result.append(1 * post_prof[i+1])

            elif i == len(nums)-1:
                result.append(pref_prod[i-1] * 1)
            
            else:
                result.append(pref_prod[i-1] * post_prof[i+1])

        return result
        