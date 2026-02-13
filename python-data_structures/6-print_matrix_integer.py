#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if  matrix == [[]] or len(matrix) == 0 or len(matrix[0]) == 0:
        print()
        return
    for row in matrix:
        for num in range(len(row)):
            if num != len(row) - 1:
                print("{:d}".format(row[num]), end=" ")
            else:
                print("{:d}".format(row[num]))
