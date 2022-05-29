input = [1, 1, 1, 0, 1, 0, 2, 2, 2, 2, 0, 1]
output = []
index = 0
for item in input:
	if item == 2:
		output.append(item)
	elif item == 1:
		output.insert(index, item)
		index += 1
	elif item == 0:
		output.insert(0, item)
		index += 1
print(output)
