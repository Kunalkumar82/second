# import Robots.MathRobot using dot operator (.)

import Robots.MathRobot
# Displaying the available operations
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
choice = input("choice (1/2/3): ")

if choice == '1':
	# call add_numbers function from the Robots.MathRobot module
	Robots.MathRobot.add_numbers()
elif choice == '2':
	# call subtract_numbers function from the Robots.MathRobot module
	Robots.MathRobot.subtract_numbers()
elif choice == '3':
	# call multiply_numbers function from the Robots.MathRobot module
	Robots.MathRobot.multiply_numbers()
else:
    print("Invalid choice")

print("Goodbye!")