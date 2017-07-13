import csv
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    shopid = []
    price = []
    product = []
    for row in readCSV:
        for the_product in row[2::]:
            shopid.append(row[0].strip())
            price.append(float(row[1].strip()))
            product.append(the_product.strip())

askProduct1, askProduct2 = raw_input('What Product do you want to buy:').split()
abc = [i for i, x in enumerate(product) if x == askProduct1]
xyz = [i for i, x in enumerate(product) if x == askProduct2]
thePrice1 = [price[p] for p in abc]
thePrice2 = [price[p] for p in xyz]
print 'the price of product1', askProduct1, 'is', thePrice1
print 'the price of product2', askProduct2, 'is', thePrice2
for i in range(len(thePrice1)):
    addition.append(thePrice1[i] + thePrice2[i])
print addition
print min(addition)
