"""

matchPattern(pattern: int[], candidate: string) → boolean
[1, 2, 1, 2], "cat dog cat dog" → true
[1, 2, 3, 2, 1], "dog ant cat ant dog" → true
[1, 2, 3, 2, 1], "dog ant cat dog dog" → false
[1, 2, 3, 400000], "ant ant ant ant" → true
[1, 2, 3, 400000, 400000], "ant ant ant ant falcon" → false

---------------

matchMetapattern(metapattern: int[][], candidate: string) → boolean
[ [1], [1, 2] ], "dog cat" → true
[ [1, 1], [1, 2] ]

[ [1, 2], [2], [1, 2] ], "ant cat falcon" → false
[ [1, 2, 1], [1, 2, 2], [2, 2, 1], [2, 2, 2] ]

[ [1, 2], [1], [1, 2] ], "dog cat cat" → true
[ [1, 1, 1], [1, 1, 2], [2, 1, 1] [2, 1, 2] ]
[ [1, 1], [2, 1] ] len(sublist) x the len(patterList)
go through and add the element from the new sublist len(patternList) many times
[ [1, 1, 1], [2, 1, 1] ]
[ [1, 1, 2], [2, 1, 2] ]

[ [1, 1, 1], [2, 1, 1], [1, 1, 2], [2, 1, 2] ]

[ [1], [1, 2], [2, 500] ], "cat dog cat" → true

"""
def matchMetapattern(metapattern, candidate):
    patterns = []
    
    for i in range(len(metapattern)): # 0, 1, 2, 3
        subTempPatterns = []
        for j in range(len(metapattern[i])):
            # tempPattern = patterns 
            if i == 0:
                subTempPatterns.append([metapattern[i][j]])
                continue
            else:
                for pattern in tempPatterns:
                    # tempPattern = patterns # [1, 2], [2,2]
                    tempPattern.append(metapattern[i][j])
            subTempPatterns.append(tempPattern)
        patterns = subTempPatterns
        print(patterns)
                    
            
    for pattern in patterns:
        if matchPattern(pattern, candidate):
            return True
    return False
                # we need to combine all the subpatterns into one pattern


def matchPattern(pattern, candidate):
    patternDict = {}
    
    canArr = candidate.strip().split()
    
    if len(pattern) != len(canArr):
        return False
    
    for i in range(len(pattern)):
        if pattern[i] not in patternDict:
            patternDict.update({pattern[i]: canArr[i]})
        # if it is in the dictionary, check that value matches
        else:
            if not patternDict.get(pattern[i]) == canArr[i]:
                return False
            
    return True

# print(matchPattern([1, 2, 3, 2, 1], "dog ant cat dog dog"))
print(gmatchMeapattern([ [1, 2], [2], [1, 2] ], "ant cat falcon"))
