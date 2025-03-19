from typing import List


def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    rowZero = False

    for r in range(num_rows):
        for c in range(num_cols):
            if matrix[r][c] == 0:
                matrix[0][c] == 0

                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    # Find the rows and columns that need to be zeroed
    for r in range(1, num_rows):
        for c in range(1, num_cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] =  0

    # Set first column to zero if applicable
    if matrix[0][0] == 0:
        for r in range(num_rows):
            matrix[r][0] = 0

    # Set first row to zero if applicable
    if rowZero:
        for c in range(num_cols):
            matrix[0][c] = 0