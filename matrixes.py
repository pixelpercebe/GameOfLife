import numpy
import copy

def st():
    row = int(input("Enter the number of rows:"))
    column = int(input("Enter the number of columns:"))
    matrix1 = []

    for rowi in range(row):
        a = []
        for columnj in range(column):
            a.append(int(input()))
        matrix1.append(a)

    # For printing the matrix
    for rowii in range(row):
        for column in range(column):
            print(matrix1[row][column], end=" ")
        print()


matrix = [[20 for column in range(2)] for row in range(5)]
print(matrix)
print(len(matrix))
new_matrix = matrix
print(matrix[1][1])
print("++++++++++++++++++++++++++++")
print(new_matrix)
new_matrix[1][0] = 2
print(new_matrix)
print(matrix)
print("++++++++++++++++++++++++++++deep copy")
new_matrix= copy.deepcopy(matrix)
new_matrix[1][0] = 6
print(new_matrix)
print(matrix)