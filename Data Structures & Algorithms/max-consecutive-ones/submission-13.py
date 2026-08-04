class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter, max = 0,0
        for digit in nums:
            if digit == 1: 
                counter += 1
            if counter > max:
                    max = counter
            if digit == 0:
                counter = 0
        return max