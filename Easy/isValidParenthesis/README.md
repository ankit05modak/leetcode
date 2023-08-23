## Objective
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


## Method 1
### Time Complexity
1. n is the length of string
2. As the loop iterated through every char from input, the time complexity becomes **O(n)**
***Overall : O(n)***

### Space Complexity
1. Only the stackList is storing values, in worst possible case it will store all values from the input.
2. The space complexity becomes **O(n)**
***Overall : O(n)***

## Method 2
### Time Complexity
**O(n)**

### Space Complexity
**O(n)**
