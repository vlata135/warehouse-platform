import os
import openpyxl
import csv
def read_csv(filename):
    map_data = []
    with open(os.path.join(filename)) as data:
        data = csv.reader(data, delimiter=",")
        for row in data:
            result_list = [int(item) if item != '' else 0 for item in row]
            print(result_list)
            map_data.append(list(result_list))
    return map_data

def matrix_to_adjacency(matrix):
    rows, cols = len(matrix), len(matrix[0])
    adjacency_matrix = [[0] * (rows * cols) for _ in range(rows * cols)]

    def index(row, col):
        return row * cols + col

    for row in range(rows):
        for col in range(cols):
            directions_list = matrix[row][col]

            for directions in directions_list:
                current_index = index(row, col)

                if 'u' in directions and row > 0:
                    adjacency_matrix[current_index][index(row - 1, col)] = 1
                if 'd' in directions and row < rows - 1:
                    adjacency_matrix[current_index][index(row + 1, col)] = 1
                if 'l' in directions and col > 0:
                    adjacency_matrix[current_index][index(row, col - 1)] = 1
                if 'r' in directions and col < cols - 1:
                    adjacency_matrix[current_index][index(row, col + 1)] = 1

    return adjacency_matrix

# Example usage:
movement_matrix = [
    [['u', 'd', 'l'], ['u', 'r', 'f']],
    [['d', 'r'], ['l', 'f']],
    [['u', 'd'], ['r', 'l']],
    [['u', 'd', 'r', 'f']]
]

data = read_csv("map2.csv")
print(data)
print(movement_matrix)
rows, cols = len(movement_matrix), len(movement_matrix[0])
print(rows, cols)
# adjacency_matrix = matrix_to_adjacency(movement_matrix)
for row in adjacency_matrix:
    print(row)
