# adder = [1,3,7,9]
# primesum = 17
# for i in range(1,199999,2):
	# for j in adder:
		# num = int(str(i)+str(j))
		# flg = False
		# for k in range(3,num//2,2):
			# if num%k==0:
				# flg = True
				# break
		# if flg==False:
			# primesum+=num
			# print(primesum)
# #print(primesum)
primesum = 5
primelist = [2,3]
inc = 1
while(1):
	primesum += 6*inc - 1
	primelist.append(6*inc - 1)
	primesum += 6*inc + 1
	primelist.append(6*inc + 1)
	if 6*inc + 1 >= 1999999:
		break
	else:
		inc+=1
print(sum(primelist))
#print(primesum)
#print(6*inc + 1)

# import eulerlib


# # Call the sieve of Eratosthenes and sum the primes found.
# def compute():
	# ans = sum(eulerlib.prime_numbers.primes(1999999))
	# return str(ans)


# if __name__ == "__main__":
	# print(compute())