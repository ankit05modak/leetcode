## Objective
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


### n & m is the length of list1 & list2 resp.
## Time Complexity
1. While loop is the major contributor to the time complexity. In the worst case, the while loop will iterate in both the lists, till the last node.
***Overall : O(n+m)***


## Space Complexity
1. Contributor to the space is current and dummy variables which takes O(1)
***Overall : O(1)***

