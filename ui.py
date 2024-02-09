import json
import random
import paho.mqtt.client as mqtt
import pygame
import os
import csv
# import button
import pandas as pd

# doc map
def read_csv(filename):
    map_data = []
    with open(os.path.join(filename)) as data:
        data = csv.reader(data, delimiter=",")
        for row in data:
            map_data.append(list(row))
    return map_data

def draw(arrVarMap):
    j = 2
    x = 0
    for point in arrVarMap:
        if x == 0:
            x += 1
            continue
        for i in range(len(point)):
            if point[i] == "":
                pygame.draw.rect(
                    screen,
                    (211, 211, 211),
                    pygame.Rect(
                        (i + 1) * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    ),
                    1,
                )
                # blit_text(screen, '+', ((i + 1) * TILE_SIZE + 4, j * TILE_SIZE), font2)
            if point[i] == "2": #diem nhan hang
                pygame.draw.rect(
                    screen,
                    (58, 232, 34),
                    pygame.Rect(
                        (i + 1) * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    ),
                )
                pygame.draw.rect(
                    screen,
                    (211, 211, 211),
                    pygame.Rect(
                        (i + 1) * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    ),
                    1,
                )
            if point[i] == "4":
                pygame.draw.rect(
                    screen,
                    (246, 181, 121),
                    pygame.Rect(
                        (i + 1) * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    ),
                )
                pygame.draw.rect(
                    screen,
                    (211, 211, 211),
                    pygame.Rect(
                        (i + 1) * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    ),
                    1,
                )
            if point[i] == "1": #diem tra hang
                pygame.draw.rect(
                    screen,
                    (58, 116, 34),
                    pygame.Rect(
                        (i + 1) * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    ),
                )
        j += 1
        

pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 1000 #1000
SCREEN_HEIGHT = 750 #900
TILE_SIZE = 10 # 12
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("demo")

arrMap = read_csv("map.csv")
df = pd.DataFrame(arrMap)
# print(df)
draw(arrMap)