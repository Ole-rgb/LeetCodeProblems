class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        keep track of the current position(to check for zero) and the position of the next non zero 
        -> two pointers

        if nums[i] == 0
        [0, 1, 0, 3, 12]
        i^  
        j^
        find first non zero to swap with and swap
        [0, 1, 0, 3, 12]
        i^  
        j   ^
        [1, 0, 0, 3, 12]
        then increase both pointers to check next element
        [1, 0, 0, 3, 12]
        i   ^  
        j      ^        
        """
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 0:
                #find next non zero then swap and increase indixes by one 
                while j<len(nums)-1 and nums[j] ==0:
                    j+=1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        