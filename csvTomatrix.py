import csv
import numpy as np
import os
# doc map
def read_csv(filename):
    map_data = []
    with open(os.path.join(filename)) as data:
        data = csv.reader(data, delimiter=",")
        for row in data:
            result_list = [int(item) if item != '' else 0 for item in row]
            # print(result_list)
            map_data.append(list(result_list))
    return map_data

# Đường dẫn của file CSV
csv_file_path = "map.csv"

# Đọc file CSV và chuyển thành ma trận
matrix_data = read_csv(csv_file_path)

# In ma trận
print(matrix_data[1][2])
