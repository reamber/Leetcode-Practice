class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = []
        
        for i in range(0, len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
            else:
                ans.remove(nums[i])
        return ans[0]
