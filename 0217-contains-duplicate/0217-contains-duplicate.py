class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
        '''
        s = {}
        for num in nums:
            if s.get(num) == True:
                return True
            s[num] = True
        return False
        '''