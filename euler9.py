import sys
for i in range(1,500):
	for j in range(1,500):
		if i < j:
			break
		else:
			if (i**2+j**2)**(1/2.0) + i + j == 1000:
				print(int(i*j*((i**2+j**2)**(1/2.0))))
				sys.exit(0)