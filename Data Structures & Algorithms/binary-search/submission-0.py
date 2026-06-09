class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def b_search(nums,target,start,end):
            if start>end:
                return -1
            mid = (end+start)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                return b_search(nums,target,start,mid-1)

            if nums[mid] < target:
                return b_search(nums,target,mid+1,end)
            
        return b_search(nums,target,0,len(nums)-1)
        