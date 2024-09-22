from multiprocessing import Pool
from time import sleep
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Линейный вызов
    start = datetime.now()
    for file in filenames:
        read_info(file)
    end = datetime.now()
    print(f'{end - start} (Линейный)')
# Многопроцессный
    start = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'{end - start} (Многопроцессорный)')