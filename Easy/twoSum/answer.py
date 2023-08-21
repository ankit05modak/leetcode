class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == int(target):
                    if i not in result:
                        result.append(i)
                    if j not in result:
                        result.append(j)
                else:
                    pass
        return result