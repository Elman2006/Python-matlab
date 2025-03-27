from matlab import Matlab 

""" Some default matrixes """
cal_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix1 = [
    [11, 22, 33],
    [44, 55, 66]
]
matrix2 = [
    [1, 2],
    [4, 5],
    [7, 8]
]

squer_matrix = [
    [11, 12],
    [33, 44]
]

# Create a new matrix with user input elements
custom_matrix = Matlab.getelement(3, 3)
print("Custom matrix:")
Matlab.printmatrix(custom_matrix)

# Create an eye and a zeros matrix with custom row and column
eye_matrix = Matlab.eye(2, 5)
Matlab.printmatrix(eye_matrix)
zeros_matrix = Matlab.zeros(4,7)
Matlab.printmatrix(zeros_matrix)

# some other usefull methods
sqrt_matrix = Matlab.sqrt(cal_matrix)
triu_matrix = Matlab.triu(matrix2)
tril_matrix = Matlab.tril(matrix2)
trace_matrix = Matlab.trace(cal_matrix) # gets only nxn matrixes
inverse = Matlab.inv(squer_matrix) # Calculating inverse of a 2x2 matrix
diag_matrix = Matlab.diag(matrix1) # diagram of a matrix [ a, b, ....]
diag_matrix_full = Matlab.diag(matrix1) # diagram of the matrix (others zero)
flip_matrix_lr = Matlab.fliplr(cal_matrix) # Flipping matrix left to right
flip_matrix_ud = Matlab.flipud(cal_matrix) # FLipping matrix upside down
rot90_matrix = Matlab.rot90_clock(matrix2)
antirot90_matrix = Matlab.rot90_anti_clock(matrix2)
determinant = Matlab.det(cal_matrix)
