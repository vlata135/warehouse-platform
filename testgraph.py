from heapq import *
# def dijkstra(start,goal,graph):
#         queue = []
#         heappush(queue, (0, start))
#         cost_visited = {start:0}
#         visited = {start: None}

#         while queue: 






def matrix_to_adjacency(matrix):
    rows, cols = len(matrix), len(matrix[0])
    print("Rows và cols là")
    print(rows, cols)
    adjacency_matrix = [[0] * (rows * cols) for _ in range(rows * cols)]

    def index(row, col):
        return row * cols + col

    for row in range(rows):
        for col in range(cols):
            directions = matrix[row][col]
            print("directions")
            print(directions)
            print("row và col")
            current_index = index(row, col)
            print(row, col)
            print("current_index")
            print(current_index)

            if 'u' in directions and row > 0:
                adjacency_matrix[current_index][index(row - 1, col)] = 1
                print("vi tri adj matrix là")
                print(index(row - 1, col))
            if 'd' in directions and row < rows - 1:
                adjacency_matrix[current_index][index(row + 1, col)] = 1
                print("vi tri adj matrix là")
                print(index(row + 1, col))
            if 'l' in directions and col > 0:
                adjacency_matrix[current_index][index(row, col - 1)] = 1
                print("vi tri adj matrix là")
                print(index(row, col - 1))
            if 'r' in directions and col < cols - 1:
                adjacency_matrix[current_index][index(row, col + 1)] = 1
                print("vi tri adj matrix là")
                print(index(row, col + 1))
            print("\n")
            print(adjacency_matrix)
            print("\n")
        

    return adjacency_matrix

# Example usage:
movement_matrix = [
    ['u', 'd', 'l'],
    ['u', 'r', 'l'],
    ['d', 'r', 'l']
]
# movement_matrix = [
    
# ]

adjacency_matrix = matrix_to_adjacency(movement_matrix)
# for row in adjacency_matrix:
    # print(row)
