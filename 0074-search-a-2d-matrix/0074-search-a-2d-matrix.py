class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            min=0
            max=len(row)-1

            if target >= row[min] and target <= row[max]:
                while min<=max:
                    mid = (min+max)//2
                    if row[mid] == target:
                        return True
                    elif target < row[mid]:
                        max = mid-1
                        
                    elif target > row[mid]:
                        min = mid+1

        return False