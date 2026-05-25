class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")":"(", "}":"{", "]":"["}

        #finish later, better solution is to uese a hashmap for 
        #the opening/closing brackets
        stack = []
        for c in s:
            if c in bracketMap:
                if stack:
                    top = stack.pop()
                else:
                    top = "placeholder"
                if (bracketMap[c]!=top):
                    return False
            else:
                stack.append(c)
            
                
        if not stack:
            return True
        else:
            return False
            
            




        