class Solution:
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Start from end due to padding
        #create end and start pointers
        end1 = m - 1 
        end2 = n - 1
        end_mn = m + n - 1 #end of nums 1 (where to write) 
        #ijk pointers
        i = end1 #iterate nums1
        j = end2 #iterate nums2
        k = end_mn #where to insert

        #insert greatest element starting from end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]: #if ith elem is greater
                nums1[k] = nums1[i] #insert ith elem
                i-=1 #decrement the contributor 
            else: #else jth is grater
                nums1[k] = nums2[j]
                j-=1
            k-=1 #move insnertion point to left 
        #if there are remainning elements in nums2 append them
        while j >= 0:
            nums1[k] = nums2[j]
            k-=1
            j-=1
        