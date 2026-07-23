class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1 #left ptr start at leftmost, R at end of nums

        while L <= R: # While search space exists
            mid = (L + R) // 2

            if target > nums[mid]: # if bigger than mid go right
                L = mid + 1 #move left to one more than mid idx
            elif target < nums[mid]: # If smaller, go left
                R = mid - 1
            else: # Otherwise target is at mid
                return mid

        #if target DNE 
        return -1