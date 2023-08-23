# Method 1
class Solution:
    def isValid(self, s: str) -> bool:
        stackList = []
        hashMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for char in s:
            if char in hashMap:
                if stackList and stackList[-1] == hashMap[char]:
                    stackList.pop()
                else:
                    return False
            else:
                stackList.append(char)
        return True if not stackList else False
            
            
# Method 2
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif stack and stack[-1] == "(" and char == ")":
                stack.pop()
            elif stack and stack[-1] == "[" and char == "]":
                stack.pop()
            elif stack and stack[-1] == "{" and char == "}":
                stack.pop()
            else:
                stack.append(char)
        return not stack
            