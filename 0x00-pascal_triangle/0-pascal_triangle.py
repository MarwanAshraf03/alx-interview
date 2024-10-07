#!/usr/bin/python3
def pascal_triangle(n):

	if n <= 0: return ([])
	# n = 10
	l_of_l = []
	for i in range(1, n+1):
		# print(l_of_l)
		if i == 1:
			l_of_l.append([1])
			continue
		new_l = [1]
		nn = 0
		if i % 2 == 0:
			# print(i)
			for j in range(1, int(len(l_of_l[i-2])/2+1)):
				# print(nn, j)
				new_l.append(l_of_l[i-2][nn] + l_of_l[i-2][j])
				nn = j
				# print(nn, j)
			new_l += list(reversed(new_l))[:]
		if i % 2 != 0:
			# print(i)
			for j in range(1, int(len(l_of_l[i-2])/2+1)):
				# print(nn, j)
				new_l.append(l_of_l[i-2][nn] + l_of_l[i-2][j])
				nn = j
				# print(nn, j)
			new_l += list(reversed(new_l[:-1]))[:]
		l_of_l.append(new_l)
	return (l_of_l)
# print(l_of_l)

# l_5 = [1, 5, 10, 10, 5, 1]

############################# when you are in an even line #############################
# l_5 = [1, 4, 6, 4, 1]
# l_5 = [1]
# l_6 = [1]
# nn = 0

# for i in range(1, int(len(l_5)/2+1)):
	# print(nn, i)
# 	l_6.append(l_5[nn] + l_5[i])
# 	nn = i
	# print(nn, i)
# print(l_5)
# print(l_6)
# l_6 += list(reversed(l_6))[:]
# print(l_6)


# print("+"*50)



############################# when you are in an odd line #############################
# l_6 = [1, 5, 10, 10, 5, 1]
# l_7 = [1]
# nn = 0

# for i in range(1, int(len(l_6)/2+1)):
	# print(nn, i)
# 	l_7.append(l_6[nn] + l_6[i])
# 	nn = i
	# print(nn, i)
# # print(l_6)
# print(l_7)
# l_7 += list(reversed(l_7[:-1]))[:]
# print(l_7)