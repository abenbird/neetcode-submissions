class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in range(len(matrix)):
            left, right = 0, len(matrix[m]) - 1
            while left <= right:
                if target > matrix[m][right]:
                    break
                mid = int((left + right) / 2)
                if matrix[m][mid] == target:
                    return True
                elif matrix[m][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False