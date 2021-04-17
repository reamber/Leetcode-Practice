class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = []
        
        zeroPresent = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroPresent+=1
            else:
                product = product*nums[i]
                
        if zeroPresent:
            for i in range(len(nums)):
                if nums[i] != 0 or zeroPresent > 1:
                    output.append(0)
                else:
                    output.append(product)
        else:
            for i in range(len(nums)):
                output.append(int(product/nums[i]))
            
        return output
        
