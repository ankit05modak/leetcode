## Objective
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

# n is length of string
## Time Complexity
1. Replace is a linear operation, so it takes **O(n)**
2. Sum and Map function both takes **O(n)**
***Overall : Dominant factor is raplace - O(n)***

## Space Complexity
1. The dictionary which is defines, takes a constant space.
2. Now the space complexity is depending upon the input s, in worst possible case, if all replacements are applied, it can be at most 4 times the length of original string.
***Overall : O(n)***

