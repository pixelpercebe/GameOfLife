import numpy
import copy
import random


def create_grid(dimensions: tuple, x_size, y_size):
    # dimensions = (columns,row)
    col = dimensions[0] // x_size
    row = dimensions[1] // y_size
    matrix = numpy.zeros((row, col))
    return matrix


def analyse_neighbours(matrix, population):
    # population = (row,col)
    neigh_count_matrix = copy.deepcopy(matrix)
    for row in neigh_count_matrix:
        for col in range(len(row)):
            row[col] = 0
    for neig in population:
        for row in range(neig[0]-1 if neig[0]-1 >= 0 else neig[0],
                         neig[0]+2 if neig[0]+1 < len(matrix) else neig[0]+1):
            for col in range(neig[1]-1 if neig[1]-1 >= 0 else neig[1],
                             neig[1]+2 if neig[1]+1 < len(matrix[1]) else neig[1]+1):
                if (row, col) == neig:
                    continue
                if matrix[row][col] == 1:
                    neigh_count_matrix[neig[0]][neig[1]] += 1
                else:
                    neigh_count_matrix[row][col] += 1
    return neigh_count_matrix


def verify_alive(old_matrix, neighbour_count_matrix):
    new_matrix = copy.deepcopy(neighbour_count_matrix)
    for row in new_matrix:
        for col in range(len(row)):
            row[col] = 0
    for row in range(len(neighbour_count_matrix)):
        for col in range(len(neighbour_count_matrix[row])):
            n = neighbour_count_matrix[row][col]
            current_state = old_matrix[row][col]
            match n:
                case _ if n < 2 or n > 3:
                    new_matrix[row][col] = 0
                case _ if current_state == 1 and n == 2:
                    new_matrix[row][col] = 1
                case _ if n == 3:
                    new_matrix[row][col] = 1
    return new_matrix


def verify_terrain(neighbour_count_matrix):
    new_matrix = copy.deepcopy(neighbour_count_matrix)
    for row in new_matrix:
        for col in range(len(row)):
            row[col] = 0
    for row in range(len(neighbour_count_matrix)):
        for col in range(len(neighbour_count_matrix[row])):
            n = neighbour_count_matrix[row][col]
            match n:
                case _ if n >= 4:
                    new_matrix[row][col] = 1
                case _ if n < 4:
                    new_matrix[row][col] = 0
    return new_matrix


def generate_random_terrain(matrix):
    population = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val = random.randint(0, 10)
            if val > 5:
                population.append((i, j))
    return population


def load_init_matrix(matrix, population):
    for i in population:
        matrix[i[0]][i[1]] = 1
    return matrix


def clean_matrix(matrix):
    for row in matrix:
        for col in range(len(row)):
            row[col] = 0
    return matrix


def print_matrix(matrix):
    print("new iteration")
    for i in matrix:
        print(i)
