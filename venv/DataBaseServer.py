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