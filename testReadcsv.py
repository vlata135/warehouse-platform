import csv

# Đường dẫn tới file CSV của bạn
csv_file_path = 'map2.csv'



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
    return arrVarMap
def createGraph()
map = read_csv(csv_file_path)
# print(len(map))
map = preProcess(map)
print(map)




                     