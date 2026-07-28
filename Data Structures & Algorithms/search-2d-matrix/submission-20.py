class Solution:
    def BinarySearch(self,matrix,L,R,target,row):
        while L <= R:
            mid = (L + R)//2
            if target > matrix[row][mid]:
                L = mid + 1
            elif target < matrix[row][mid]:
                R = mid - 1
            else:
                return mid
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
       
        m = len(matrix)      # number of rows
        n = len(matrix[0])   # number of columns

        if m == 1 and n == 1:
            if target == matrix[0][0]:
                return True
            else: 
                return False


        i = 0
        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][n-1]:
                if self.BinarySearch(matrix,0,n-1,target,i) != -1:
                    return True
   
        return False
