import timeit
from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        row_len = len(matrix[0])
        idx = -1
        while matrix:
            row = matrix.pop(0)
            left = 0
            right = row_len - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] > target:
                    right = mid - 1
                elif row[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    break
            if idx != -1:
                return True
        
        return False
        
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        matrix_len = len(matrix) - 1
        row = 0
        col = len(matrix[0]) - 1

        while row <= matrix_len and col >= 0:
            if target == matrix[row][col]:
                return True
            
            if target < matrix[row][col]:
                # 더 작은 값과 비교하기 위해 열을 좌측으로 이동
                col -= 1
            elif target > matrix[row][col]:
                # 더 큰 값과 비교하기 위해 행을 아래로 이동
                row += 1
        return False
        
    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)



s = Solution()
print(timeit.timeit(lambda: s.searchMatrix(
    [
        [1,4,7,11,15, 31, 32, 33],
        [2,5,8,12,19, 34, 35, 36],
        [3,6,9,16,22, 37, 38, 39],
        [10,13,14,17,24, 40, 41, 42],
        [18,21,23,26,30, 43, 44, 45],
        [46,49,50,51,52, 54, 57, 59],
        [47,48,53,54,55, 56, 57, 58],
    ], 54), number=100000))
print(timeit.timeit(lambda: s.searchMatrix2(
    [
        [1,4,7,11,15, 31, 32, 33],
        [2,5,8,12,19, 34, 35, 36],
        [3,6,9,16,22, 37, 38, 39],
        [10,13,14,17,24, 40, 41, 42],
        [18,21,23,26,30, 43, 44, 45],
        [46,49,50,51,52, 54, 57, 59],
        [47,48,53,54,55, 56, 57, 58],
    ], 54), number=100000))
print(timeit.timeit(lambda: s.searchMatrix3(
    [
        [1,4,7,11,15, 31, 32, 33],
        [2,5,8,12,19, 34, 35, 36],
        [3,6,9,16,22, 37, 38, 39],
        [10,13,14,17,24, 40, 41, 42],
        [18,21,23,26,30, 43, 44, 45],
        [46,49,50,51,52, 54, 57, 59],
        [47,48,53,54,55, 56, 57, 58],
    ], 54), number=100000))