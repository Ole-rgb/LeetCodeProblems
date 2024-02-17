class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max=len(nums)-1
        min=0
        
        while min<=max:
            i = (min+max)//2
            
            if nums[i] < target:
                min = i+1
            elif nums[i] > target:
                max = i-1

            else:
                return i

        return -1