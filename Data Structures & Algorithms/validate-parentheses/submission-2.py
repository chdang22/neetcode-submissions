class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #store open bracket types
        for char in s:
            if char == '(' or char == '{' or char == '[' :
                #if is open bracket type, add to stack
                stack.append(char)
            elif stack: #otherwise it is closed type
            #first check if stack is not empty
                #if the closing does not have matching open bracket in stack
                #return false as rule 2 or 3 is not met
                if (char == ')' and stack.pop() != '(') or \
                    (char == '}' and stack.pop() != '{') or \
                    (char == ']' and stack.pop() != '['):
                    return False
            else: return False #stack is empty, rule 3 not met
        if not stack:
            #if stack is empty, then all 3 rules met
            return True
        else:
            #if stack not empty, rule 1 has not been met
            return False


            
