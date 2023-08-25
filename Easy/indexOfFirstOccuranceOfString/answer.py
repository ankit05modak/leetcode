class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack)):
            if needle == haystack[i:i+len(needle)]:
                index = i
                break
        return index