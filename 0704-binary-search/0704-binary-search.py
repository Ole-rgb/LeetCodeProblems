class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        mid = (min+max)//2

        while min <= max:
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                min = mid+1

            elif nums[mid] > target:
                max = mid-1

            mid = (min+max)//2        
        return -1