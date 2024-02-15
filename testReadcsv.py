import csv

# Đường dẫn tới file CSV của bạn
csv_file_path = 'map_test.csv'


def matrix_to_adjacency(matrix):
    rows, cols = len(matrix), len(matrix[0])
    print("Rows và cols là")
    print(rows, cols)
    adjacency_matrix = [[0] * (rows * cols) for _ in range(rows * cols)]

    def index(row, col):
        return row * cols + col

    for row in range(rows):
        for col in range(cols):
            directions = matrix[row][col]
            print("directions")
            print(directions)
            print("row và col")
            current_index = index(row, col)
            print(row, col)
            print("current_index")
            print(current_index)

            if 'u' in directions and row > 0:
                adjacency_matrix[current_index][index(row - 1, col)] = 1
                print("vi tri adj matrix là")
                print(index(row - 1, col))
            if 'd' in directions and row < rows - 1:
                adjacency_matrix[current_index][index(row + 1, col)] = 1
                print("vi tri adj matrix là")
                print(index(row + 1, col))
            if 'l' in directions and col > 0:
                adjacency_matrix[current_index][index(row, col - 1)] = 1
                print("vi tri adj matrix là")
                print(index(row, col - 1))
            if 'r' in directions and col < cols - 1:
                adjacency_matrix[current_index][index(row, col + 1)] = 1
                print("vi tri adj matrix là")
                print(index(row, col + 1))
            print("\n")
            print(adjacency_matrix)
            print("\n")
    return adjacency_matrix

def read_csv(filename):
    map_data = []
    with open(csv_file_path, "r") as data:
        data = csv.reader(data, delimiter=",")
        for row in data:
            map_data.append(list(row))
    return map_data

def preProcess(arrVarMap):
    map = []
    for col in range(len(arrVarMap)):
         for item in range(len(arrVarMap[0])):
            if(len(arrVarMap[col][item])>2):
                char = ""
                if "u" in arrVarMap[col][item]: char = char + "1"
                else: char = char + "0"
                if "d" in arrVarMap[col][item]: char = char + "1"
                else: char = char + "0"
                if "r" in arrVarMap[col][item]: char = char + "1"
                else: char = char + "0"
                if "l" in arrVarMap[col][item]: char = char + "1"
                else: char = char + "0"
                arrVarMap[col][item] = char
                # print(arrVarMap[col][item])
    return arrVarMap
def createGraph(map):
    rows, cols = len(map), len(map[0])
    adjacency_matrix = [[0] * (rows * cols) for _ in range(rows * cols)]
    for col in range(len(map)):
        for item in range(len(map[0])):
            if len(map[col][item]) > 3:
                if (map[col][item][0]) == "1":
                    adjacency_matrix[col + 1][item] = 1

                if(map[col][item][1]) == "1":
                    adjacency_matrix[col - 1][item] = 1
                
                if(map[col][item][2]) == "1":
                    adjacency_matrix[col][item + 1] = 1
                
                if(map[col][item][3]) == "1":
                    adjacency_matrix[col][item - 1] = 1
            else: 
                adjacency_matrix[col + 1][item] = 0
                adjacency_matrix[col - 1][item] = 0
                adjacency_matrix[col][item + 1] = 0
                adjacency_matrix[col][item - 1] = 0

    return  adjacency_matrix
    
map = read_csv(csv_file_path)
# print(len(map))
# map = preProcess(map)
# print(map[3][4][0])
# alo = createGraph(map)
print(map)
# print(alo[5][9])
adj_matrix = matrix_to_adjacency(map)



                     