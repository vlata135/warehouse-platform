import pygame as pg
from random import random
from collections import deque
import os
import csv
import numpy as np

SCREEN_WIDTH = 1000 #1000
SCREEN_HEIGHT = 780  #900

# TILE = 40
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

def draw(arrVarMap):
    for i in range(len(arrVarMap)):
        for j in range(len(arrVarMap[0])):
            if arrVarMap[i][j] == 0:
                pg.draw.rect(sc, pg.Color('gray'), get_rect(j, i), border_radius=TILE // 5)
                rect1 = pg.Rect(get_rect(j,i))
                # pg.draw.circle(sc, pg.Color('blue'), (j * TILE + 1, i * TILE + 1), 2)
                pg.draw.circle(sc, pg.Color('blue'),rect1.center, 2)
            if arrVarMap[i][j] == 1:
                pg.draw.rect(sc, pg.Color('red'), get_rect(j, i), border_radius=TILE // 5)
            if arrVarMap[i][j] == 2:
                pg.draw.rect(sc, pg.Color('yellow'), get_rect(j, i), border_radius=TILE // 5)
            if arrVarMap[i][j] == 3:
                pg.draw.rect(sc, pg.Color('blue'), get_rect(j, i), border_radius=TILE // 5)
            if arrVarMap[i][j] == 4:
                pg.draw.rect(sc, pg.Color('green'), get_rect(j, i), border_radius=TILE // 5)    
            

cols, rows = 28, 28
TILE = 20

pg.init()
sc = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("demo")
clock = pg.time.Clock()
# grid
# grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]
# print(grid)

grid = read_csv("map.csv")
print(grid)
# dict of adjacency lists
graph = {}
# for y, row in enumerate(grid):
#     for x, col in enumerate(row):
#         if not col:
#             graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

# BFS settings
start = (0, 0)
queue = deque([start])
visited = {start: None}
cur_node = start

while True:
    # fill screen
    sc.fill(pg.Color("black"))
    # draw grid
    # [[pg.draw.rect(sc, pg.Color('darkorange'), get_rect(x, y), border_radius=TILE // 5)
    #   for x, col in enumerate(row) if col] for y, row in enumerate(grid)]
    draw(grid)
    # pygame necessary lines
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)