class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

 Vjlekm
    def get_products(self):
        file = open(self.__file_name, 'r')
        prod_list = file.read()
        file.close()
        return prod_list

    def add(self, *products: Product):
        prods_in_shop = self.get_products()
        f_opened = False
        for pr_ in products:
            if pr_.name not in (lst_.split(', ')[0] for lst_ in prods_in_shop.splitlines() ):
                if not f_opened:
                    file = open(self.__file_name, 'a')
                    f_opened = True
                file.write(str(pr_) + '\n')
            else:
                print(f'Продукт {pr_.name} уже есть в магазине.')

        if f_opened:
            file.close()



if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())


