import csv
import sys

def read_csv_cell(file_path, row_num, col_num):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        try:
            cell_value = data[row_num][col_num]
            print(cell_value)
        except IndexError:
            print("Ошибка: указанная строка или столбец выходит за пределы таблицы")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python read_csv_cell.py <путь_к_csv_файлу> <номер_строки> <номер_столбца>")
    else:
        file_path = sys.argv[1]
        row_num = int(sys.argv[2])
        col_num = int(sys.argv[3])
        read_csv_cell(file_path, row_num, col_num)

