class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n > 2:
#             return (self.climbStairs(n-2) + self.climbStairs(n-1))
        
#         return n
        
    
    def __init__(self):
        
        self.cache = {}
    
    def climbStairs(self, n):    
        
        if n in self.cache:
            return self.cache[n]
        
        if n == 0 or n == 1:
            return 1
        
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.cache[n] = result
            return result
