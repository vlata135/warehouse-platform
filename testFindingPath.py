from queue import Queue

def bfs(graph, start, end):
    # Khởi tạo Queue để lưu trữ các đỉnh cần duyệt
    queue = Queue()
    
    # Khởi tạo mảng visited để kiểm tra đỉnh đã được duyệt hay chưa
    visited = [False] * len(graph)
    
    # Mảng để lưu trữ đỉnh trước đỉnh hiện tại trong đường đi ngắn nhất
    predecessor = [-1] * len(graph)
    
    # Bắt đầu từ đỉnh start
    queue.put(start)
    visited[start] = True
    
    while not queue.empty():
        current_vertex = queue.get()
        
        # Duyệt qua các đỉnh kề của đỉnh hiện tại
        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor] = True
                predecessor[neighbor] = current_vertex
    
    # Truy vết đường đi từ end đến start
    path = []
    current_vertex = end
    
    while current_vertex != -1:
        path.insert(0, current_vertex)
        current_vertex = predecessor[current_vertex]
    
    return path

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}

start_vertex = 0
end_vertex = 4

shortest_path = bfs(graph, start_vertex, end_vertex)

print("Shortest path from {} to {}:".format(start_vertex, end_vertex))
print(shortest_path)
