class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1 
        
        while l <= r:
            mid = (l + r) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][0] and target > matrix[mid][-1]:
                l = mid + 1
            else:
                for n in matrix[mid]:
                    if n == target:
                        return True
                return False

        return False