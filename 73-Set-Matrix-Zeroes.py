class Solution(object):
    def setZeroes(self, matrix):
        \\\
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        \\\
        m, n = len(matrix), len(matrix[0])
        
        # Determine if the first row and first column should be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row and first column to mark zero rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out cells based on the markers in the first row and column
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

        