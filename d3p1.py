counter = 8
num = 1
input_num = 325489
num_list = []

while num < 525489:
	num_list.append(num)
	num += counter
	counter += 8

max_num_in_layer = min(filter(lambda x: x > input_num,num_list))
print('Answer:', max_num_in_layer - input_num)