primelist = [2,3,5,7]
adder = [1,3,7,9]
inc = 1
while(1):
	for i in adder:
		num = int(str(inc)+str(i))
		flg = False
		for j in range(3,num//2,2):
			if num%j==0:
				flg = True
				break
		if flg==False:
			primelist.append(num)
			#print(num)
			
	inc+=1
	if len(primelist)==10001:
		print(primelist[10000])
		break