num = [[1, 2], [3], [4, 5, 6]]


def nested_sum(t):
   # sums = []
	total = 0
	for i in t:
		for j in i:
			total += j
     #   sums.append(total)
	print(total)

nested_sum(num)
