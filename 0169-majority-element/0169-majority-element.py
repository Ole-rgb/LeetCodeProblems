class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = defaultdict(int)
        n = len(nums) // 2

        for num in nums:
            
            elements[num] += 1 

            if elements[num] > n:
                return num
        