class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = arr[len(arr)-1] #set max to last element
        for i in range(len(arr)-1, -1, -1): #start at second to last of arr and iterate leftward
        #range(start,stop,step) stop value is exclusive, stops before hitting it
            
            if  arr[i-1] > max_so_far: #if to the left of i is greater than the curr max.
                prev_max = max_so_far #store pmax before updating
                max_so_far = arr[i-1] #update max 
                arr[i-1] = prev_max #change arr[i-1] to prev max

                #dont update arr[i]
            else: #if curr max is still bigger than element to left of i, overwrite the element to the left
                arr[i-1] = max_so_far

        arr[len(arr)-1] = -1 #replace last element with -1 as per directions 
        return arr
 