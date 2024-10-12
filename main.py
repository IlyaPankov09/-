import requests
import pandas as pd
import numpy as np

class Requests:
    url = 'https://prokupol.ru'
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        data = r.url
        print(f'Статус ответа: OK')
    else:
        print('Ошибка при выполнении запроса')


class Panda:
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
    df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        })
    print(df2)

    # data = pd.read_fwf(r'C:\Users\Илья\PythonProjects\modul_11_1\Readme')
    # print(data)

class Numpy:
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Создаем массив
    print(a)
    a[0] = 10
    print(a)
    sum = np.sum(a)   # Суммируем его элементы
    flip = np.flip(a) # Элементы массива в обратном порядке

    print(sum)
    print(flip)
