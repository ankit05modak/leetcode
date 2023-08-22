# Method 1
class Solution:
    def longestCommonPrefix(self, strs):
        strs = sorted(strs)
        ans = ""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if (strs[0][i] != strs[-1][i]):
                return ans
            ans += strs[0][i]
        return ans
    
# Method 2
class Solution:
    def longestCommonPrefix(self, strs):
        response = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                response += a[0]
            else:
                return response
        return response