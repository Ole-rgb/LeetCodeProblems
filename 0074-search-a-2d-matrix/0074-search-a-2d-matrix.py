class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            min=0
            max=len(row)-1

            if  !(target >= row[min] and target <= row[max]):
                continue

            while min<=max:
                mid = (min+max)//2

                if target < row[mid]:
                    max = mid-1
                    continue
                if target > row[mid]:
                    min = mid+1
                    continue
                
                return True

        return False