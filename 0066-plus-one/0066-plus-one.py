class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #option one: read, then increment, then write
        
        #option two: increment in the array, without extracting the number 
        #base case only increase lsb by one
        #if lsb == 9 -> set to 0 and repeat for bit to the left
        num = self.parse_int(digits)
        res = self.write(num+1)
        print(res)
        return res
        

    def parse_int(self, digits: List[int]) -> int:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10**(len(digits)-i-1))
        return num
    
    def write(self, num: int) -> List[int]:
        l = list()
        
        while num > 0:
            l.append(num % 10)
            num //= 10
        
        l.reverse()
        return l
