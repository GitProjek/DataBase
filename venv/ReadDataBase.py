import pickle
from Objects import Product

with open('products.txt', encoding='UTF-8') as data:
    data_base = []
    while True:
        product = data.readline()
        if not product:
            break
