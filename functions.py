import numpy


def create_grid(dimensions: tuple,x_size,y_size):
    # dimensions = (columns,row)
    col = dimensions[0] // x_size
    row = dimensions[1] // y_size
    matrix = numpy.zeros((row, col))
    print(row, col)
    return matrix

def analyse_neighbours(matrix, population):
    neigh_count_matrix = numpy.zeros((len(matrix),len(matrix)))
    for neig in population:
        for row in range(neig[0]-1, neig[0]+1):
            if row == -1:
                continue
            for col in range(neig[1]-1, neig[1]+1):
                if col == -1:
                    continue
                matrix[row][col] = 2;


        # for cells in range(neig[0]-1,neig[0]+1):
        #   for
