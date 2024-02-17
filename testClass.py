from env import *

SCREEN_WIDTH = 1000 #1000
SCREEN_HEIGHT = 780  #900
TILE = 23

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("demo")
clock = pg.time.Clock()

path_matrix_map = "mapCheck.csv"
path_matrix_moveRule = "map_test.csv"
data = Data(path_matrix_moveRule,path_matrix_map)

matrix_map = data.read_csv_to_draw_map()
matrix_moveRule = data.read_csv_to_draw_graph()

graph = Graph(matrix_moveRule)
adjacency_list = graph.adjacency_matrix_to_adjacency_list()

algorithm = Algorithm(adjacency_list,matrix_moveRule)
start = 0
end = 125
path = algorithm.Astar(adjacency_list,start,end)
print(path)

draw = Draw(screen,matrix_map,TILE=23)


while True:
    # fill screen
    screen.fill(pg.Color("black"))
    # draw grid
    # [[pg.draw.rect(sc, pg.Color('darkorange'), get_rect(x, y), border_radius=TILE // 5)
    #   for x, col in enumerate(row) if col] for y, row in enumerate(grid)]
    draw.draw_background()
    draw.drawPath(path,draw.getPosition())
    # pygame necessary lines
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)