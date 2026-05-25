class Solution:
    def isValid(self, s: str) -> bool:
        def bracketSort(bracket):
            if (bracket == "["):
                return 1
            if (bracket == "{"):
                return 2
            if (bracket == "("):
                return 3
            if (bracket == "]"):
                return -1
            if (bracket == "}"):
                return -2
            if (bracket == ")"):
                return -3
        
        stack = []
        for c in s:
            if (bracketSort(c)>0):
                stack.append(c)
            elif (bracketSort(c)<0):
                if stack:      
                    if (bracketSort(stack[-1]) + bracketSort(c) == 0):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        if not stack:
            return True
        else:
            return False
            
            




        