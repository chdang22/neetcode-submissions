class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            match op:
            
                case "+": #add two prev scores
                    stack.append(stack[-1] + stack[-2])
                    #^why start -1? Because -1 is the last element and -2 is the second to last
                case "D": #double prev score
                    stack.append(stack[-1] * 2)
                case "C": #invalidate prev score
                    stack.pop()
                case _:
                    stack.append(int(op))
        total_sum = sum(stack)
        return total_sum