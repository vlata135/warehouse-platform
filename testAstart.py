import heapq

def heuristic_manhattan(node, end_node):
    # Hàm heuristic Mahattan cho A*
    x1, y1 = node
    x2, y2 = end_node
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(adjacency_list, start, end):
    inf = float('inf')

    # Khởi tạo mảng khoảng cách và đỉnh cha
    dist = {vertex: inf for vertex in adjacency_list}
    parent = {vertex: None for vertex in adjacency_list}

    # Đỉnh xuất phát có khoảng cách là 0
    dist[start] = 0

    # Hàng đợi ưu tiên để lựa chọn đỉnh có khoảng cách ngắn nhất
    priority_queue = [(0, start)]

    while priority_queue:
        cur_dist, u = heapq.heappop(priority_queue)

        # Duyệt qua các đỉnh kề của u
        for v, edge_weight in adjacency_list[u]:
            new_dist = dist[u] + edge_weight

            # Cập nhật khoảng cách và đỉnh cha nếu có đường đi ngắn hơn
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                # Sử dụng hàm heuristic Mahattan để tối ưu hóa A*
                priority = new_dist + heuristic_manhattan(v, end)
                heapq.heappush(priority_queue, (priority, v))

    # Truy vết đường đi ngắn nhất từ end về start
    path = []
    cur_node = end
    while cur_node is not None:
        path.insert(0, cur_node)
        cur_node = parent[cur_node]

    return path

# Ví dụ sử dụng
graph_adjacency_list = {
    (0, 0): [((0, 1), 2), ((1, 0), 4)],
    (0, 1): [((1, 1), 1), ((0, 2), 7)],
    (1, 0): [((1, 1), 3)],
    (1, 1): []
}

start_node = (0, 0)
end_node = (1, 1)

shortest_path = a_star(graph_adjacency_list, start_node, end_node)
print("Đường đi ngắn nhất:", shortest_path)
