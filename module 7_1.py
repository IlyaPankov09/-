from pprint import pprint
class Product:

    def __init__(self, name, weight, category,):
        self.name = name
        self.weidht = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weidht}, {self.category}'
class Shop():
    __file_name = 'products.txt'

    lines = []
    product_names = []
    def get_products(self):
        file = open(__file_name, 'r')
        pprint(file.read())
        file.close()

    def __add__(self, *products):
        file = open(__file_name, 'a')
        for file in products:
            lines.uppend(file)
            product_names.uppend(self.name)
            if name in product_names:
                print(f'Продукт {self.name} уже есть в магазине')
            else:
                file.write(f'\n{self.__file_name}')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())