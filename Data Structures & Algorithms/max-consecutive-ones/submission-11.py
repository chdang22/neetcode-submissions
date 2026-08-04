class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_max, prev_max = 0,0
        for digit in nums:
            if digit == 1: 
                cur_max += 1
            if cur_max >= prev_max:
                    prev_max = cur_max
            if digit == 0:
                cur_max = 0
        return prev_max