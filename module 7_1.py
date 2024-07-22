from pprint import pprint
class Product:

    def __init__(self, name, weight, category,):
        self.name = name
        self.weidht = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weidht}, {self.category}'
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(__file_name, 'r')
        pprint(file.read())
        file.close()
        # file.close()

    def __add__(self, *products):
        file = open(__file_name, 'a')
        file.write(self.__file_name)
        for name in products:
            if name == self.name:
                print(f'Продукт {self.name} уже есть в магазине')
            else:
                file.uppend(name)

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())