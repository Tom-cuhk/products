
products = []
while True:
	name = input('Please input the product name: ')
	print('Press q to quit the input')
	if name == 'q': #quit the input
		break
	price = input('Please input the product price: ')
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
		f.write(p[0] + ',' + p[1] + '\n')