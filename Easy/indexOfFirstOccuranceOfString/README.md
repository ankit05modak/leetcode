## Objective
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack

## Time Complexity
1. The main cause of time is the for loop. The loop iterates  through each char of haystack. 
2. In the worst possible case, the haystack can be very large as compared to needle, and the match could be found at the last or not found at all till the last index.
3. This makes time complexity **O(len(haystack) * len(needle))**

## Space Complexity
1. The space remains constant throughout the process, hence **O(1)**

