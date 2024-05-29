my_dict = {'Ilya': 1987, 'Dasha': 1989, 'Anna': 2020}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Katya'))
my_dict.update({'Mather': 1964, 'Father': 1963})
print(my_dict.pop('Ilya'))
print(my_dict)
my_set= {1,2,3,4,2,3,'ilya',3,4,4}
print(my_set)
print(my_set.add('anna'))
print(my_set.add(8))
print(my_set)
my_set.discard('ilya')
print(my_set)