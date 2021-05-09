class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        left = 0
        right = 1
        output = 1
        
        letterSet = set()
        letterSet.add(s[left])
        
        while right < len(s):
            letterSet.add(s[right])
            while len(letterSet) != len(s[left:right + 1]):
                letterSet.remove(s[left])
                left += 1
                letterSet.add(s[right])
            
            if (len(s[left:right + 1])) > output:
                output = (len(s[left:right + 1]))
                
            right += 1
                
                
        return output
