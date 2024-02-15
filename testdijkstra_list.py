import sys
import csv
import time
csv_file_path = 'map_test.csv'

from heapq import *
def read_csv(filename):
    map_data = []
    with open(csv_file_path, "r") as data:
        data = csv.reader(data, delimiter=",")
        for row in data:
            map_data.append(list(row))
    return map_data

def matrix_to_adjacency(matrix):
    rows, cols = len(matrix), len(matrix[0])
    adjacency_matrix = [[0] * (rows * cols) for _ in range(rows * cols)]

    def index(row, col):
        return row * cols + col

    for row in range(rows):
        for col in range(cols):
            directions = matrix[row][col]
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

def matrix_to_adjacency_list(matrix):
    adjacency_list = {}

    for i in range(len(matrix)):
        neighbors = []
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                neighbors.append((j, matrix[i][j]))
        adjacency_list[i] = neighbors

    return adjacency_list

def dijkstra(adjacency_list, start, end):
    inf = float('inf')

    # Khởi tạo mảng khoảng cách và đỉnh cha
    dist = {vertex: inf for vertex in adjacency_list}
    parent = {vertex: None for vertex in adjacency_list}

    # Đỉnh xuất phát có khoảng cách là 0
    dist[start] = 0

    # Hàng đợi ưu tiên để lựa chọn đỉnh có khoảng cách ngắn nhất
    priority_queue = [(0, start)]

    while priority_queue:
        cur_dist, u = heappop(priority_queue)

        # Duyệt qua các đỉnh kề của u
        for v, edge_weight in adjacency_list[u]:
            new_dist = cur_dist + edge_weight

            # Cập nhật khoảng cách và đỉnh cha nếu có đường đi ngắn hơn
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heappush(priority_queue, (new_dist, v))

    # Truy vết đường đi ngắn nhất từ end về start
    path = []
    cur_node = end
    while cur_node is not None:
        path.insert(0, cur_node)
        cur_node = parent[cur_node]

    return path

# Ví dụ sử dụng
#đọc map dưới dạng movement move ( u,d,r,l)
map = read_csv(csv_file_path)
#chuyển map về dạng ma trận kề
adj_matrix = matrix_to_adjacency(map)
adj_list = matrix_to_adjacency_list(adj_matrix)
start_node = 0
end_node = 125
t1 = time.time()
shortest_path = dijkstra(adj_list, start_node, end_node)
t2 = time.time()
print("Đường đi ngắn nhất:", shortest_path)
print("Thoi gian thuc hien")
print(t2 - t1)