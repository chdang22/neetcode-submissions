import math

class Solution:
    
    def quickSort(self,arr, s: int, e: int) -> list[int]:
        if s >= e:
            return
        pivot = arr[e] # pivot is last element
        left = s # ptr for left side

        # data[i][0] is the distance for comparison
        # and data[i][1] is the original [x, y]

        # partition: elements smaller than pivot on left side
        for i in range(s, e):

            # Instead of comparing arr[i] < pivot:
            if arr[i][0] < pivot[0]:#access and compare the distance
                arr[left], arr[i] = arr[i], arr[left]
                left += 1 # Increment left

        # Move pivot in between left and right sides
        arr[e] = arr[left] # left is in middle so swap to pivot spot
        arr[left] = pivot # Now move pivot to middle

        #QuickSort left
        self.quickSort(arr, s, left - 1)
        #Quicksort right
        self.quickSort(arr,left+1,e)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data = []
        # Now data[i][0] is the distance for comparison
        # and data[i][1] is the original [x, y]

        for p in points:
            #store point with distance
            dist = p[0]**2 + p[1]**2 #use this forumla bc origin
            data.append([dist, p])
        # quicksort list of ans
        s = 0
        e = len(data)-1

        self.quickSort(data,s,e)
        result = [point for dist, point in data[:k]]
        return result