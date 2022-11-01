number = input("Guess the number: ")

while (int(number) != 42):
	if (int(number) < 42):
		print("Too low!")
		number = input("Guess the number: ")
	elif (int(number) > 42):
		print("Too high!")
		number = input("Guess the number: ")

print("Correct!")
	
