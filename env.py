import pygame as pg
from random import random
from collections import deque
import os
import csv
import numpy as np
from heapq import *
import time

class Graph:
    def __init__(self, matrix_moveRule):
        self.matrix_moveRule = matrix_moveRule
        self.adjacency_matrix = self.matrix_moveRule_to_adjacency_matrix
    
    def matrix_moveRule_to_adjacency_matrix(self):
        rows, cols = len(self.matrix_moveRule), len(self.matrix_moveRule[0])
        adjacency_matrix = [[0] * (rows * cols) for _ in range(rows * cols)]

        def index(row, col):
            return row * cols + col

        for row in range(rows):
            for col in range(cols):
                directions = self.matrix_moveRule[row][col]
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
    def adjacency_matrix_to_adjacency_list(self):
        adjacency_list = {}
        adjacency_matrix = self.adjacency_matrix()
        for i in range(len(adjacency_matrix)):
            neighbors = []
            for j in range(len(adjacency_matrix[i])):
                if adjacency_matrix[i][j] > 0:
                    neighbors.append((j, adjacency_matrix[i][j]))
            adjacency_list[i] = neighbors

        return adjacency_list
    
    def getCoordinate(matrix_moveRule, index):
        rows, cols = len(matrix_moveRule), len(matrix_moveRule[0])
        row = index // cols
        col = index % cols
        return row, col
    
class Data:
    def __init__(self, path_matrix_moveRule, path_matrix_map):
        self.path_matrix_moveRule = path_matrix_moveRule
        self.path_matrix_map = path_matrix_map

    def read_csv_to_draw_map(self):
        map_data = []
        with open(self.path_matrix_map) as data:
            data = csv.reader(data, delimiter=",")
            for row in data:
                result_list = [int(item) if item != '' else 0 for item in row]
                # print(result_list)
                map_data.append(list(result_list))
        return map_data
    
    def read_csv_to_draw_graph(self):
        map_data = []
        with open(self.path_matrix_moveRule, "r") as data:
            data = csv.reader(data, delimiter=",")
            for row in data:
                # map_data.append(list(row))
                result_list = [item for item in row if item != '']
                map_data.append(list(result_list))
        return map_data

class Algorithm:
    def __init__(self, adjacency_list,matrix_moveRule):
        self.adjacency_list = adjacency_list
        self.matrix_moveRule = matrix_moveRule

    def getCoordinate(self, index):
        rows, cols = len(self.matrix_moveRule), len(self.matrix_moveRule[0])
        row = index // cols
        col = index % cols  
        return row, col
    
    def heuristic_manhattan(self, node, end_node):
        # Hàm heuristic Mahattan cho A*
        x1, y1 = self.getCoordinate(node)
        x2, y2 = self.getCoordinate(end_node)
        return abs(x1 - x2) + abs(y1 - y2)

    def Astar(self,adjacency_list, start, end):
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
                    priority = new_dist + self.heuristic_manhattan(v, end)
                    heappush(priority_queue, (priority, v))
                    # heappush(priority_queue, (new_dist, v))

        # Truy vết đường đi ngắn nhất từ end về start
        path = []
        cur_node = end
        while cur_node is not None:
            path.insert(0, cur_node)
            cur_node = parent[cur_node]

        return path
    
class Draw:
    def __init__(self, screen, matrix_map, TILE):
        self.screen = screen
        self.matrix_map = matrix_map
        self.TILE = TILE

    def get_rect(self, x, y):
        return x * self.TILE + 1, y * self.TILE + 1 , self.TILE - 2, self.TILE - 2
    
    def draw_background(self):
        for i in range(len(self.matrix_map)):
            for j in range(len(self.matrix_map[0])):
                rect1 = pg.Rect(self.get_rect(j,i))
                if self.matrix_map[i][j] == 0:
                    pg.draw.rect(self.screen, pg.Color('gray'), self.get_rect(j, i), border_radius=self.TILE // 5)
                    # rect1 = pg.Rect(get_rect(j,i)) 
                    # pg.draw.circle(sc, pg.Color('blue'), (j * TILE + 1, i * TILE + 1), 2)
                    # pg.draw.circle(sc, pg.Color('blue'),rect1.center, 2)
                if self.matrix_map[i][j] == 1:
                    pg.draw.rect(self.screen, pg.Color('red'), self.get_rect(j, i), border_radius=self.TILE // 5)
                    # rect2 = pg.Rect(get_rect(j,i))
                if self.matrix_map[i][j] == 2:
                    pg.draw.rect(self.screen, pg.Color('yellow'), self.get_rect(j, i), border_radius=self.TILE // 5)
                if self.matrix_map[i][j] == 3:
                    pg.draw.rect(self.screen, pg.Color('blue'), self.get_rect(j, i), border_radius=self.TILE // 5)
                if self.matrix_map[i][j] == 4:
                    pg.draw.rect(self.screen, pg.Color('green'), self.get_rect(j, i), border_radius=self.TILE // 5)    
    
    def getPosition(self):    
        center = []
        for i in range(len(self.matrix_map)):
            for j in range(len(self.matrix_map[0])):
                rect1 = pg.Rect(self.get_rect(j,i))
                center.append(rect1.center)  
        # center = matrix_to_array(center)
        # print(center[1])
        return center
    
    def drawPath(self,path,centers):
        for point in path:
            pg.draw.circle(self.screen, pg.Color('blue'), centers[point], 4)


class Agent:
    def __init__(self, velocity, path):
        self.velocity = velocity
        self.path = path

    def move(self):
        
    