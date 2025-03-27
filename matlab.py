class Matlab:
    """ All matlab matrix functions"""

    def getelement(row, column):
        """Create and return a new matrix with user input elements."""
        matrix = []
        for i in range(row):
            row_data = []
            for j in range(column):
                val = float(input(f"Enter row {i+1}, column {j+1} element: "))
                row_data.append(val)
            matrix.append(row_data)
        return matrix

    def printmatrix(matrix):
        """Print a matrix with elements centered in a 5-character width."""
        for row in matrix:
            print(" ".join(f"{elem:^9.4f}" for elem in row))

    def cpy_matrix(matrix):
        """ A function to copy matrix to another variable """
        return [row.copy() for row in matrix]
    
    def eye(row, column):
        """Create and return an identity matrix."""
        return [[1 if i == j else 0 for j in range(column)] for i in range(row)]
    
    def zeros(row, column):
        """Create and return a matrix of zeros."""
        return [[0] * column for _ in range(row)]
    
    def sqrt(matrix):
        """Return a NEW matrix with square roots of elements (preserves original)."""
        return [[elem ** 0.5 for elem in row] for row in matrix]
    
    def triu(matrix):
        """ Upper triangular matrix (zero below diagonal)."""
        return [
            [elem if i <= j else 0 for j, elem in enumerate(row)]
            for i, row in enumerate(matrix)
        ]

    def tril(matrix):
        """Lower triangular matrix (zero above diagonal)."""
        return [
            [elem if i >= j else 0 for j, elem in enumerate(row)]
            for i, row in enumerate(matrix)
        ]
    
    def trace(matrix) -> float:
        """Calculate the trace of a square matrix (sum of diagonal elements)."""
        if not matrix or len(matrix) != len(matrix[0]):
            raise ValueError("Matrix must be square (n x n).")
        return sum(matrix[i][i] for i in range(len(matrix)))
    
    def inv(matrix):
        """Calculate the inverse of a 2x2 matrix with validation."""
        if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
            raise ValueError("Input must be a 2x2 matrix.")
        
        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
        det = a * d - b * c
        if det == 0:
            raise ValueError("Matrix is singular (determinant = 0).")
        
        return [
            [ d / det, -b / det ],
            [ -c / det, a / det ]
        ]
    
    def diag(matrix):
        """Extract the main diagonal elements of a square matrix"""
        return [matrix[i][i] for i in range(len(matrix))]

    def diag_matrix(matrix):
        """Create a matrix with only diagonal elements (others zero)"""
        size = len(matrix)
        return [[matrix[i][j] if i == j else 0 for j in range(size)] 
                for i in range(size)]
    
    def fliplr(matrix):
        """A function to flip the matrix from left to right"""
        if not matrix:
            return []
        return [row[::-1] for row in matrix]
    
    def flipud(matrix):
        """Flip matrix up-down (reverse row order)"""
        return matrix[::-1]
    
    def rot90_clock(matrix):
        """ A function to rotate the matrix 90 degrees in clock way"""
        return [list(row) for row in zip(*matrix[::-1])]
    
    def rot90_anti_clock(matrix):
        """Rotate matrix 90° counter-clockwise using zip."""
        return [list(row) for row in zip(*matrix)][::-1]
    
    def det(self, matrix):
        """Calculate the determinant of a square matrix."""
        # Ensure the matrix is square
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix must be square (n x n).")
        
        # Base case: 1x1 matrix
        if len(matrix) == 1:
            return matrix[0][0]
        
        # Base case: 2x2 matrix
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        # Recursive case: n x n matrix
        determinant = 0
        for col in range(len(matrix)):
            # Create a submatrix by excluding the first row and the current column
            submatrix = [
                row[:col] + row[col+1:]  # Exclude the current column
                for row in matrix[1:]   # Exclude the first row
            ]
            # Recursive call and apply cofactor (-1)^(row+column)
            determinant += ((-1) ** col) * matrix[0][col] * self.det(submatrix)
        
        return determinant
       
