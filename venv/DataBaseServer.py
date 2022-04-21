import pickle
from Objects import Product

data = open('products.dat', '+rb')
products_data = pickle.load(data)
while True:
    print("Введите номер операции для работы с БД:")
    print('1 - Корректировка/дополнение данных БД')
    print('2 - Сортировка БД по названию/общей стоимости')
    print('3 - Вывод данных о товаре/товарах из БД')
    print('4 - Сохранить БД как')
    print('5 - Выход')
    com = int(input())
    if com == 1:
        print("Введите номер операции для работы с данными:")
        print('1 - Корректировать данные')
        print('2 - Добавить данные')
        com = int(input())
        if com == 1:
            prod = input("Введите название продукта для работы с ним:").lower()
            work = None
            while True:
                for i in products_data:
                    if i.title == prod:
                        work = i
                        break
                if not work:
                    print("Товар не найден. Повторите попытку снова.")
                    prod = input("Введите название продукта для работы с ним:").lower()
                else:
                    break
            print("Введите параметр продукта, который будет корректироваться:")
            print('1 - Название')
            print('2 - Стоимость единицы товара')
            print('3 - Количество')
            print('4 - Единица измерения')
            com = int(input())
            print(work.title)
            if com == 1:
                work.title = input('Введите новое название продукта:').lower()
                print(work.title)
            elif com == 2:
                work.cost = input('Введите новую цену продукта:').lower()
            elif com == 3:
                work.quantity = input('Введите количество продукта:').lower()
            elif com == 4:
                work.unit_of_measure = input('Введите новую единицу измерения продукта:').lower()