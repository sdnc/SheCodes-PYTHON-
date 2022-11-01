# MOTH EXERCISE

moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
	print("Hoooman, help me get the moths!")
if not  moths_in_house and not mitch_is_home:
	print("No threats detected.")
if moths_in_house and not mitch_is_home:
	print("Meooooooow! Hisssss!")
if not moths_in_house and mitch_is_home:
	print("Climb on Mitch.")


# TALL ENOUGH? EXERCISE

height = input("Wanna go for a ride? Please enter your height in cm (number only): ")

if int(height) < 120:
	print("Sorry, not today :(")
else:
	print("Hop on!")

# EMAIL LOGIN

email = input("Enter your email address: ")

if "@" in email and "." in email:
	print("Valid email address")
else:
	print("Invalid email address")
