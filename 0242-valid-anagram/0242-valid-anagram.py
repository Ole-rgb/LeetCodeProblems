from collections import defaultdict 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        d = defaultdict(lambda: 0)
        for i in range(0,len(s)):
            d[s[i]] = d[s[i]] + 1
            d[t[i]] = d[t[i]] - 1
        
        for value in d.values():
            if value != 0:
                return False
        return True