import sys
import csv
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

def dijkstra(matrix, start, end):
    n = len(matrix)
    inf = float('inf')

    # Khởi tạo mảng khoảng cách và đỉnh cha
    dist = [inf] * n
    parent = [-1] * n

    # Đỉnh xuất phát có khoảng cách là 0
    dist[start] = 0

    # Hàng đợi ưu tiên để lựa chọn đỉnh có khoảng cách ngắn nhất
    priority_queue = [(0, start)]

    while priority_queue:
        cur_dist, u = heappop(priority_queue)

        # Duyệt qua các đỉnh kề của u
        for v in range(n):
            if matrix[u][v] > 0:  # Kiểm tra có cạnh nối từ u đến v hay không
                new_dist = cur_dist + matrix[u][v]

                # Cập nhật khoảng cách và đỉnh cha nếu có đường đi ngắn hơn
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
                    heappush(priority_queue, (new_dist, v))

    # Truy vết đường đi ngắn nhất từ end về start
    path = []
    cur_node = end
    while cur_node != -1:
        path.insert(0, cur_node)
        cur_node = parent[cur_node]

    return path

# Ví dụ sử dụng
#đọc map dưới dạng movement move ( u,d,r,l)
map = read_csv(csv_file_path)
#chuyển map về dạng ma trận kề
adj_matrix = matrix_to_adjacency(map)

start_node = 0
end_node = 15

shortest_path = dijkstra(adj_matrix, start_node, end_node)

print("Đường đi ngắn nhất:", shortest_path)