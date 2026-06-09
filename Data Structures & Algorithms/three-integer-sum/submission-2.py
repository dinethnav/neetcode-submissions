class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_result = []

        i = 0

        while i< len(nums)-2:
            j = i+1
            k = len(nums) - 1

            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue

            while j<k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    final_result.append([nums[i],nums[j],nums[k]])
                    while j<k-1 and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
        

                    
                elif total> 0:
                    while k>j+1 and nums[k] == nums[k-1]:
                        k-=1
                    k-=1

                else:
                    while j<k-1 and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
                    
            i+=1

        return final_result
                

            
     