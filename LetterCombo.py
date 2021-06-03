class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsArr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        output = []
        
        for num in digits:
            tempOutput = []
            for char in digitsArr[int(num)]:
                if len(output) == 0:
                    tempOutput.append(char)
                    continue
                for combo in output:
                    tempOutput.append(combo + char)

            output = tempOutput
                
        return output
