data_structure = [[1, 2, 3],{'a':4, 'b':5},(6,{'cube':7,'drum':8}),"Hello",((),[{(2,'Urban',('Urban2',35))}])]
#print(len(data_structure))
# for i in data_structure:
#     print(type(i))
def calculate_structure_sum(data_structure):
    summa = 0
    for i in data_structure:
        if isinstance(i, (list, tuple, set)):
            summa += calculate_structure_sum(i)
        elif isinstance(i, str):
            summa += len(data_structure)
        elif isinstance(i, (int, float)):
            summa += i
        elif isinstance(i, dict):
           for key, value in i.items():
                summa += calculate_structure_sum(key)
                summa += calculate_structure_sum(value)
    return summa
print(calculate_structure_sum(data_structure))


# print(len(data_structure))
# for i in data_structure:
#     #print(type(i))
#     def index():
#         new_list = list(i)
#         return new_list
#     print(index())
#     print(type(i))




#def calculate_structure_sum():



#result = calculate_structure_sum(data_structure)
#print(result)