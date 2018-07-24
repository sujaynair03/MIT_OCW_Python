print("-----------PART 1")
for n in range(1, 11):
	print (1.0/n)
	n = float(n)

print("-----------PART 2")
a = input("Give me a positive number: ")
while a >= 0:
    print(a)
    a -= 1

print ("-----------PART 3")
base = input("Give me a base: ")
exp = input("Give me an exponent: ")
base = int(base)
exp = int(exp)
print( base**exp)

print ("------------PART 4")
while True:
	x = input("Give me an even number: ")
	if x %2 == 0:
		print ("Good Job")
		break
	else:
		print ("Try again")