import io
from pprint import pprint
def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding= 'utf-8') as file:
        for line in strings:
            enumLine = enumerate(line)
            for key in enumLine:
                j = key
            file.write(line +'\n')
            byte = file.tell()
            strings_positions[j, byte] = line
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
