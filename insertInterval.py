class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        newStart = newInterval[0]
        newEnd = newInterval[1]
        
        overlapStart = newStart
        overlapEnd = newEnd
        
        added = False
        
        for subList in intervals:
            start = subList[0]
            end = subList[1]
            
            # if entire interval is smaller, just append
            if end < newStart:
                ans.append(subList)
            
            # if entire interval is bigger, just append
            elif newEnd < start:
                if not added:
                    ans.append([overlapStart, overlapEnd])
                    added = True
                ans.append(subList)
            
            # if there is overlap
            else:
                overlapStart = min(start, overlapStart)
                overlapEnd = max(end, overlapEnd)
        
        if not added:
            ans.append([overlapStart, overlapEnd])
        
        return ans
