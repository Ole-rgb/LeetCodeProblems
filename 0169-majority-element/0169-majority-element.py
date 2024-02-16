class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}

        for num in nums:
            key = "{}".format(num)
            elements[key] = 1 if elements.get(key) == None else elements.get(key)+1

            if elements[key] > math.floor((len(nums)/2)):
                return num
        