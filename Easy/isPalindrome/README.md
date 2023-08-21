## Objective 
Given an integer x, return true if x is a palindrome, and false otherwise.

# n is length of input & x is the value of integer
## Time complexity
1. Converting an integer to a string - **O(log(x))**
2. Reversing - **O(n)**
3. Comparison - **O(n)**
***Overall == O(log(x) + n)***

## Space complexity
1. String conversion - **O(log(x))**
2. Two temporary strings - **O(n)**
***overall == O(log(x) + n)***
