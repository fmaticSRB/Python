##########################################################
# Author: Filip Matic
# Title: ArrayCheck.py
# Description: Program checks if a value exists in the array
##########################################################

# Initialize List
List = [1, 2, 3, 4, 5, 6]

#Value to find
check = 4

print("Checking if {1} exists in the list", check)

#Use for loop
for x in List:
	if x == check:
		print("True")
		break

# Using in command alone
if x == check:
	print("True")

