'''

Convert Roman numeral string to integer value

Input: IX
Output: 9
IX is a Roman symbol which represents 9 

Input: XL
Output: 40
XL is a Roman symbol which represents 40

Input: MCMIV
Output: 1904
M is a thousand, 
CM is nine hundred and 
IV is four


SYMBOL       VALUE
  I            1
  IV           4
  V            5
  IX           9
  X            10
  XL           40
  L            50
  XC           90
  C            100
  CD           400
  D            500
  CM           900 
  M            1000

'''

def romanToNum(roman):
    romanDict = {}
    romanDict.update({'I': 1})
    romanDict.update({'V': 5})
    romanDict.update({'X': 10})
    romanDict.update({'L': 50})
    romanDict.update({'C': 100})
    romanDict.update({'D': 500})
    romanDict.update({'M': 1000})
    
    value = 0
    
    for i in range(len(roman)):
        j = i + 1
        if j < len(roman):
            if romanDict[roman[i]] < romanDict[roman[j]]:
                value -= romanDict[roman[i]]
                continue
        value += romanDict[roman[i]]
    
    return value

print(romanToNum("MCMVI"))
