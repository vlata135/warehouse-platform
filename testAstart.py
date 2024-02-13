from heapq import *

graph = {'A': [(2, "M"), (3, "P")],
         "M": [(2, "A"), (2, "N")],
         "N": [(2, "M"), (2, "B")],
         "B": [(2, "N"), (4, "P")],
         "P": [(3, "A"), (4, "B")]}

def dijkstra(start, goal, graph):
    queue = []
    heappush(queue, (0, start))  # push start to the queue
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node

    return visited

start = "A"
goal = "B"
visited = dijkstra(start, goal, graph)

path = []
cur_node = goal
while cur_node != start:
    path.append(cur_node)
    cur_node = visited[cur_node]

path.append(start)
print(pa)
# Print the reversed path
print(f'Path from {start} to {goal}:')
print(' ---> '.join(reversed(path)))
