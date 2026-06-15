class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+": #add two prev scores
                    stack.append(stack[-1] + stack[-2])
            elif op == "D": #double prev score
                    stack.append(stack[-1] * 2)
            elif op == "C": #invalidate prev score
                    stack.pop()
            else:
                    stack.append(int(op))
        total_sum = sum(stack)
        return total_sum