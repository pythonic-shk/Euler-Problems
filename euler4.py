import sys
for x in range(999999,100001,-1):
	y = str(x)
	if y == y[::-1]:
		for i in range(999,100,-1):
			if x%i==0 and len(str(int(x/i)))==3:
				print(x)
				#print(i)
				#print(int(x/i))
				sys.exit()