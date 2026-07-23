class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # arr only containns 0,1,2
        counts = [0,0,0]

        # count quantity of each val in arr
        for n in nums:
            counts[n] += 1
        
        # fill each bucket in og arr
        i = 0 #pts to og arr for writing
        for n in range(len(counts)): #traverse count
            for j in range(counts[n]): #write i to bucket n times at each i the  
                nums[i] = n
                i += 1
        

        