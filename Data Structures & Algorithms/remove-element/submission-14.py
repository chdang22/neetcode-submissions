class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count=0
        nums_length = len(nums)
        j = nums_length - 1 
        i = 0
        while i <= j:
            if nums[i] == val:
                while nums[j] == val and j>i:
                    j-= 1
                    val_count += 1
                nums[i] = nums[j]
                val_count += 1
                j -= 1
            i += 1
            
        k = nums_length - val_count
        return k