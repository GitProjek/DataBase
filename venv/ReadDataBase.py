import pickle
from Objects import Product

with open('products.txt', encoding='UTF-8') as data:
    data_base = []
    while True:
        product = data.readline()
        if not product:
            break
        prd = Product()
        prd.title, prd.cost, prd.quantity, prd.unit_of_measure = product.split()
        data_base.append(prd)
        print(prd.title, prd.cost, prd.quantity, prd.unit_of_measure)
    data_file = open('products.dat', 'wb')
    pickle.dump(data_base, data_file)
    data_file.close()
