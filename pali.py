new_string = int(input())
new_string2 = str(new_string)
lead_zero = '0'
count = 0

if new_string == new_string2[::-1]:
	print('Yes')

else:
	for i in new_string2[::-1]:
		if i != lead_zero:
			break
		if i == lead_zero:
			count += 1

	n2 = count * lead_zero + new_string2

	if n2 == n2[::-1]:
		print('Yes')
	else:
		print('No')


