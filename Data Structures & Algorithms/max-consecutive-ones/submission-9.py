class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        counter = 0
        for element in nums:
            if element == 1:
                counter+=1
            else:
                if counter>max:
                    max = counter
                counter = 0
        if counter>max:
            max=counter
        return max