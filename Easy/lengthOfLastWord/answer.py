# Method 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
# Method 2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()[::-1]
        n = 0
        for i in range(len(string)):
            if string[i] != " ":
                n += 1
            else:
                return n
        return n
        
# Method 3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a, b = 0, 0
        s += " "
        for i in range(len(s)):
            if s[i] != " ":
                b += 1
            else:
                if b > 0:
                    a = b
                b = 0
        return a

