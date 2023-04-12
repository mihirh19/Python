"""In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a
different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns
of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""
from typing import List
import numpy as np
import itertools


class Solution2:
    def matrixReshape2(self, mat: List[List[int]], r: int, c: int) -> object | list[list[int]]:
        try:
            return np.reshape(mat, (r, c)).tolist()
        except:
            return mat


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if row * col != r * c:
            return mat

        val = [v for ro in mat for v in ro]
        res = [[0 for _ in range(c)] for _ in range(r)]

        k = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = val[k]
                k += 1
        return res


if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 4
    c = 1

    # s = Solution2()
    s2 = Solution()
    # print(s.matrixReshape2(mat, r, c))

    print(s2.matrixReshape(mat, r, c))
