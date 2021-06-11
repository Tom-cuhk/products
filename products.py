
products = []
while True:
	name = input('Please input the product name: ')
	print('Press q to quit the input')
	if name == 'q': #quit the input
		break
	price = input('Please input the product price: ')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)
	products.append(p)


print(products)
# print(products[0][0])

for product in products:
	print(product)
	print('The price of ', product[0], 'is ', product[1] )


with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

with open('products.csv', 'w') as f: #csv file could be opened by excel, and the data is commonly separately by ','
	f.write('Product name' + ',' + 'Product price' + '\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') 