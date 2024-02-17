import pygame as pg
from random import random
from collections import deque
import os
import csv
import numpy as np
from heapq import *
import time
from function import *

SCREEN_WIDTH = 1000 #1000
SCREEN_HEIGHT = 780  #900

# TILE = 40

    

cols, rows = 28, 28
TILE = 23

pg.init()
sc = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("demo")
clock = pg.time.Clock()
# grid
# grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]
# print(grid)

grid = read_csv("map2_unmark.csv")
map = read_csv_algo('map_test.csv')
map2 = read_csv("mapCheck.csv")
# print(map)
centers = getPosition(map2)
#chuyển map về dạng ma trận kề
adj_matrix = matrix_to_adjacency(map)
adj_list = matrix_to_adjacency_list(adj_matrix)
start_node = 62
end_node = 75
t1 = time.time()
shortest_path = dijkstra(adj_list, start_node, end_node)
print("Đường đi ngắn nhất:", shortest_path)
t2 = time.time()
print("Thoi gian thuc hien")
print(t2 - t1)

while True:
    # fill screen
    sc.fill(pg.Color("black"))
    
    draw(grid)
    drawMove(shortest_path,centers)
    # pygame necessary lines
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)