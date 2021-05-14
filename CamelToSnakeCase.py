
# expecting a raw JSON object to be passed in
def solution(raw):
    snakeDict = {}
    
    for key, val in raw.items():    
        snakeStr = ""
        for char in key:
            if char == "-":
                if snakeStr != "":
                    snakeStr += "_"
                    continue
            elif char.isupper():
                if snakeStr != "":
                    snakeStr += "_"
            elif char.isnumeric():
                if snakeStr != "" and not snakeStr[-1].isdigit():
                    snakeStr += "_"
            snakeStr += char.lower()
        
        if type(val) is dict:
            val = solution(val)
        elif type(val) is list:
            snakeArray = []
            for ele in val:
                if type(ele) is dict:
                    ele = solution(ele)
                snakeArray.append(ele)
            val = snakeArray
        
        snakeDict.update({snakeStr: val})
    
    return snakeDict
