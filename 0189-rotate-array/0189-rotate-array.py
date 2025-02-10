class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        [4, 8, 6, 3, 2] tmp = 4
         ^
         
        [4, 8, 4, 3, 2] tmp = 6
               ^
        [4, 8, 4, 3, 6] tmp = 2
                     ^
        [4, 2, 4, 3, 6] tmp = 8
            ^         
        [4, 2, 4, 8, 6] tmp = 3
                  ^ 
        [3, 2, 4, 8, 6] tmp = 4
         ^      -> TERMINATE index == start_index
         
        always jump ahead k steps to write the next number
        then do the same from the index that was last written to 
        - use mod to wrap around bounds
        -> O(1) space
        -> O(n) time
        
        PROBLEM: circles if len(nums) and k both even or odd
        
        OTHER APPROACH:
        ->Reverse from hint#3
        [1, 2, 3, 4, 5] k = 2
        
        REVERSE THE ENTIRE ARRAY
        [5, 4, 3, 2, 1] k = 2
        
        REVERSE THE FIRST k ELEMENTS
        [4, 5,  |   3, 2, 1] k = 2
        REVERSE THE REMAINING ELEMENTS len(nums)-k
        [4, 5,  |   1, 2, 3] k = 2
        '''
        #ensure length constraints
        k = k % len(nums)
        
        
        #reverse array
        rotate(nums, 0, len(nums)-1)

        # 1. reverse 0 to k
        rotate(nums, 0, k-1)

        # 2. reverse len(nums)-k to len(nums)
        rotate(nums, k, len(nums)-1)


            
def rotate(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
            