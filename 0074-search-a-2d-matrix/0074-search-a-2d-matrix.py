class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            min=0
            max=len(row)-1

            if target >= row[min] and target <= row[max]:
                while min<=max:
                    mid = (min+max)//2

                    if target < nums[mid]:
                        max = mid-1
                        continue
                    if target > nums[mid]:
                        min = mid+1
                        continue
                    
                    return True

        return False

    def number_in_row(self, nums:List[int],target: int)->bool:
        min = 0
        max = len(nums)-1
        
        while min<=max:
            mid = (min+max)//2

            if target < nums[mid]:
                max = mid-1
                continue
            if target > nums[mid]:
                min = mid+1
                continue
            
            return True

        return False