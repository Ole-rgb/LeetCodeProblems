class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = self.parse_int(digits)
        res = self.write(num+1)
        return res
        

    def parse_int(self, digits: List[int]) -> int:
        num = 0
        for i in range(len(digits)): #O(n)
            num += digits[i] * (10**(len(digits)-i-1))
        return num
    
    def write(self, num: int) -> List[int]:
        l = list()
        while num > 0: #O(n)
            l.append(num % 10)
            num //= 10
        
        l.reverse() #max O(n)
        return l
