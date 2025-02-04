class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if d.get(f"{num}", None) is not None:
                del  d[f"{num}"] 
                continue

            d[f"{num}"] = 1
        
        for key in d.keys():
                return int(key)