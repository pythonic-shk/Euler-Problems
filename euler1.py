n = input("Enter n: ")
multiples = []
for i in range(int(n)):
	if i%3 == 0 or i%5 == 0:
		multiples.append(i)
print("Multiples of 3 or 5 or both are ",multiples)
print("Sum of Multiples of ",n," Numbers is ",sum(multiples))