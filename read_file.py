name = input('Please input your product name: ')
products = []
with open('products.csv', 'r') as f:
	for line in f:
		s = line.strip().split(',')
	#	print(s)
		if s[0] == name:
			print('Your price of your product is ', s[1])
		products.append(s)
print(products)