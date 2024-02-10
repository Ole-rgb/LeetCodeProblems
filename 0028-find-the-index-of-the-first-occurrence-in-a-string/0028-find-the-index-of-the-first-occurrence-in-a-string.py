class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        for i in range(0, len(haystack) - len(needle) + 1):
            sub = haystack[i : i + len(needle)]

            if sub == needle:
                return i

        return res
