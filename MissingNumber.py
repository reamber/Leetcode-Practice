class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        
        # ordered = [None] * n
        
#         for i in range(len(nums)):
#             ordered[nums[i]] = True
        
#         for j in range(len(ordered)):
#             if ordered[j] == None:
#                 return j
        
