import numpy


def create_grid(dimensions: tuple, x_size, y_size):
    # dimensions = (columns,row)
    col = dimensions[0] // x_size
    row = dimensions[1] // y_size
    matrix = numpy.zeros((row, col))
    print(row, col)
    print(len(matrix)-1,len(matrix[1])-2)
    return matrix


def analyse_neighbours(matrix, population):
    ##population = (row,col)
    neigh_count_matrix = numpy.zeros((len(matrix),len(matrix)))
    for neig in population:
        for row in range(neig[0]-1 if neig[0]-1 >= 0 else neig[0],
                         neig[0]+2 if neig[0]+1 < len(matrix) else neig[0]+1):
            for col in range(neig[1]-1 if neig[1]-1 >= 0 else neig[1],
                             neig[1]+2 if neig[1]+1 < len(matrix[1]) else neig[1]+1):
                if (row,col) == neig:
                    continue
                ##if matrix[row][col] == 1:
                    ##neigh_count_matrix[neig[0]][neig[1]] += 1
                matrix[row][col] = 2

