## Objective
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

### n is the length of string
# Method 1
## Time Complexity
1. sorted function takes **O(n*log(n))** time. 
2. rest of the computations are not dominant in time complexity.
***Overall : O(n*log(n))***

## Space Complexity
1. ans variable stores the longest common suffix. In the worst case, it could be as long as the shortest string in the list.
***Overall : O(min length of strings)***

### n is length of string, m is length of longest string
# Method 2
## Time Complexity
1. In this method, I learnt about zip(*variable) function, which creates a tuple containing all characters of the string.
   e.g : input("string") => output(("s", "t", "r", "i", "g"))
   (Also, try it for list type input to know more.)
2. The time complexity is dominated by zip function **O(n * m)**

## Space Complexity
1. Only the response variable stores the longest common prefix, in the worst possible case, it could be as long as the shortest possible string in the list input provide. - **O(min length of strings)**

