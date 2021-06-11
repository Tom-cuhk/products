
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
