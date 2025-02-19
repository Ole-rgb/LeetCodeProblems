class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #   find first non zero and swap with first position, then find next non zero and swap to second position, ...
        j = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            #swap 
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            j += 1
                