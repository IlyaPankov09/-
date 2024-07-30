import os
import time
print(os.getcwd())
# directory = 'C:\Modul_7'

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file},\n'
              f' Путь: {filepath},\n'
              f' Размер: {filesize} байт,\n'
              f' Время изменения: {formatted_time},\n'
              f' Родительская директория: {parent_dir}')