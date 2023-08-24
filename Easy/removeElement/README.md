## Objective
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

* Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
* Return k.

## Method 1
### Time Complexity
1. List comprehension iterated through every element of the list. Time complexity becomes **O(n)**

### Space Complexity
1. In the worst case, the new list will have same size that of original list. - **O(n)**

## Method 2
### Time Complexity
1. In while loop, the list gets iterated through every element, also when it pop(), in the reassignment of positions in the actual list, it again gets iterated.
2. Due to use of pop(), the time complexity becoms **O(n^2)**

### Space Complexity
1. As this method does not create a new list, the space remains same throughout the process - **O(1)**

