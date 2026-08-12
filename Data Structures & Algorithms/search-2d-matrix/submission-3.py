class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] <= target and matrix[row][-1] >= target:
                break
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                top = row + 1
        
        if top > bottom:
            return False
        
        matrix_row = matrix[row]
        l, r = 0, len(matrix_row) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix_row[mid] == target:
                return True
            elif matrix_row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False