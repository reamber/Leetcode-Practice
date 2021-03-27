class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setNum = set(nums)
        return len(setNum) < len(nums)
