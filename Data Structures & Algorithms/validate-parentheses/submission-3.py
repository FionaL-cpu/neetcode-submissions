class Solution:
    def isValid(self, s: str) -> bool:
        #edge cases 
        if not s: 
            return False 
        closeToOpen = {}
        closeToOpen["]"] = "["
        closeToOpen[")"] = "("
        closeToOpen["}"] = "{"
        
        stack = []
        for i in range(len(s)):
            if s[i] in closeToOpen: #close brackets 
                if stack and stack[-1] == closeToOpen[s[i]]: #value matches open one 
                    stack.pop()
                else:
                    return False 
            # open brackets 
            else:
                stack.append(s[i])


        if not stack: 
            return True 
        else: 
            return False
