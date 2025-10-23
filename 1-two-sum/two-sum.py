class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  # store number: index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

        