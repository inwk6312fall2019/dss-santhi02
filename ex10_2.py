num = [1, 2, 3, 4, 5, 6]


def cumsum(t):
	sums = []
	total = 0
	for i in t:
		total += i
		sums.append(total)
	print(sums)

cumsum(num)
