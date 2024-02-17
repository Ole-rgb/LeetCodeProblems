class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max=len(nums)-1
        min=0
        
        while min<=max:
            mid = (min+max)//2
            
            if nums[mid] < target:
                min = mid+1
            elif nums[mid] > target:
                max = mid-1

            else:
                return mid

        return -1