#n = 600851475143
n = 13195
i = 2
while i * i < n:
	while n % i == 0:
		n = n / i
		print(n,":",i)
	i = i + 1
print(n)