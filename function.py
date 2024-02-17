import pygame as pg
from random import random
from collections import deque
import os
import csv
import numpy as np
from heapq import *
import time

SCREEN_WIDTH = 1000 #1000
SCREEN_HEIGHT = 780  #900
TILE = 23

def read_csv_algo(filename):
    map_data = []
    with open(filename, "r") as data:
        data = csv.reader(data, delimiter=",")
        for row in data:
            # map_data.append(list(row))
            result_list = [item for item in row if item != '']
            map_data.append(list(result_list))
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
def getCoordinate(matrix, index):
    rows, cols = len(matrix), len(matrix[0])
    row = index // cols
    col = index % cols
    return row, col
def heuristic_manhattan(map,node, end_node):
    # Hàm heuristic Mahattan cho A*
    x1, y1 = getCoordinate(map,node)
    x2, y2 = getCoordinate(map,end_node)
    return abs(x1 - x2) + abs(y1 - y2)

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
                # Sử dụng hàm heuristic Mahattan để tối ưu hóa A*
                priority = new_dist + heuristic_manhattan(v, end)
                heappush(priority_queue, (priority, v))
                # heappush(priority_queue, (new_dist, v))

    # Truy vết đường đi ngắn nhất từ end về start
    path = []
    cur_node = end
    while cur_node is not None:
        path.insert(0, cur_node)
        cur_node = parent[cur_node]

    return path
def read_csv(filename):
    map_data = []
    with open(os.path.join(filename)) as data:
        data = csv.reader(data, delimiter=",")
        for row in data:
            result_list = [int(item) if item != '' else 0 for item in row]
            # print(result_list)
            map_data.append(list(result_list))
    return map_data

def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1 , TILE - 2, TILE - 2

def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def draw(sc,arrVarMap):
    center = []
    for i in range(len(arrVarMap)):
        for j in range(len(arrVarMap[0])):
            rect1 = pg.Rect(get_rect(j,i))
            center.append(rect1.center)
            if arrVarMap[i][j] == 0:
                pg.draw.rect(sc, pg.Color('gray'), get_rect(j, i), border_radius=TILE // 5)
                # rect1 = pg.Rect(get_rect(j,i)) 
                # pg.draw.circle(sc, pg.Color('blue'), (j * TILE + 1, i * TILE + 1), 2)
                # pg.draw.circle(sc, pg.Color('blue'),rect1.center, 2)
            if arrVarMap[i][j] == 1:
                pg.draw.rect(sc, pg.Color('red'), get_rect(j, i), border_radius=TILE // 5)
                # rect2 = pg.Rect(get_rect(j,i))

            if arrVarMap[i][j] == 2:
                pg.draw.rect(sc, pg.Color('yellow'), get_rect(j, i), border_radius=TILE // 5)
            if arrVarMap[i][j] == 3:
                pg.draw.rect(sc, pg.Color('blue'), get_rect(j, i), border_radius=TILE // 5)
            if arrVarMap[i][j] == 4:
                pg.draw.rect(sc, pg.Color('green'), get_rect(j, i), border_radius=TILE // 5)    
    return center

def getPosition(arrVarMap):
    
    def matrix_to_array(matrix):
        array = []

        for row in matrix:
            array.extend(row)

        return array
    
    center = []
    for i in range(len(arrVarMap)):
        for j in range(len(arrVarMap[0])):
            rect1 = pg.Rect(get_rect(j,i))
            center.append(rect1.center)  
    # center = matrix_to_array(center)
    # print(center[1])
    return center

def drawMove(sc,path,centers):
    for point in path:
        pg.draw.circle(sc, pg.Color('blue'), centers[point], 4)