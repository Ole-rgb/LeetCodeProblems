class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        """
        => find every substring of len(needle) in haystack
        1. start at index zero (->to zero+len(needle)) 
        then increase the counter by one until index+len(needle) = len(haystack)
        2. compare substring to needle 
        """
        for i in range(0, len(haystack) - len(needle) + 1):
            sub = haystack[i : i + len(needle)]

            if sub == needle:
                return i

        return res
