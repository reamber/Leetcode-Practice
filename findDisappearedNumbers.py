class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check = [i for i in range(len(nums) + 1)]
        ans = []
        
        for j in range(len(nums)):
            check[nums[j]] = 0
            
        for k in range(len(check)):
            if check[k] != 0:
                ans.append(check[k])
                
        return ans
        
