class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        def row_search(start ,end):

            mid = (start + end)//2

            if start>end:
                return -1
            
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return mid
            
            if target > matrix[mid][-1]:
                return row_search(mid+1,end)

            if target < matrix[mid][0]:
                return row_search(start,mid-1)

        def col_search(r,start,end):
            mid = (start + end) //2

            if start>end:
                return False
            
            cval = matrix[r][mid]
            
            if cval == target:
                return True
            
            if cval > target:
                return col_search(r,start,mid-1)
            
            if cval < target:
                return col_search(r,mid+1,end)



        r = row_search(0,m-1)
        if r == -1:
            return False
        c = col_search(r,0,n-1)

        return c
        