"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from turtle import left
from typing import List
import datetime


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        def searchMatrix(lo, hi, row):
            if lo > hi: return False
            mid = (lo + hi) // 2
            if row is not None:
                if matrix[row][mid] == target: return True
                if target > matrix[row][mid]: return searchMatrix(mid + 1, hi, row)
                return searchMatrix(lo, mid - 1, row)
            if target < matrix[mid][0]: return searchMatrix(lo, mid - 1, row)
            if target > matrix[mid][-1]: return searchMatrix(mid + 1, hi, row)
            return searchMatrix(0, len(matrix[0]) - 1, mid)

        return searchMatrix(0, len(matrix) - 1, None)


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    t = datetime.datetime.now()
    print(Solution().searchMatrix(matrix, target))
    print(datetime.datetime.now() - t)
