"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        valueDict = {}
        subDict = {}
        
        for employee in employees:
            valueDict.update({employee.id: employee.importance})
            subDict.update({employee.id: employee.subordinates})
        
        self.calcValue(valueDict, subDict, id)
                       
        return valueDict[id]
            
    def calcValue(self, valueDict, subDict, id):
        if subDict[id] == []:
            return valueDict[id]
        else:
            totalValue = valueDict[id]
            for sub in subDict[id]:
                totalValue += self.calcValue(valueDict, subDict, sub)
            valueDict.update({id: totalValue})
            return totalValue
        
