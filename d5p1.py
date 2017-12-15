with open('d5.txt') as fp:
   file = fp.readlines()


for line in file:
	if line.strip() == '0':
		print(1)
		