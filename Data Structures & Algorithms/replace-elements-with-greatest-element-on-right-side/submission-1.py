class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = arr[len(arr)-1] #set max to last element
        for i in range(len(arr)-2, -1, -1): #start at second to last of arr and iterate leftward
        #range(start,stop,step) stop value is exclusive, stops before hitting it
                prev_max = max_so_far
                max_so_far = max(max_so_far,arr[i])

                arr[i] = prev_max    
                

        arr[len(arr)-1] = -1 #replace last element with -1 as per directions 
        return arr
 