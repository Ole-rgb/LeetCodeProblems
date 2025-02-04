class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #constant space??? -> remove pairs?->still = O(n/2)
        #linear runtime -> one for loop over the array to find the number
        d = dict()
        for num in nums:
            d[f"{num}"] = d.get(f"{num}", 0)+1
        
        for key, value in d.items():
            if value == 1:
                return int(key)