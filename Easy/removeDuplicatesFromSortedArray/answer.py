# Method 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(sorted(set(nums)))
        return len(nums)
    

# Method 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            if nums[i] != nums[a]:
                a += 1
                nums[a] = nums[i]
        return a + 1