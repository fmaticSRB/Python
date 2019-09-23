##########################################################
# Author: Filip Matic
# Title: factorial.py
# Description: This is a basic code that finds factorial
# of a number
##########################################################

def factorial(n):

	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n-1);

#Driver code
num = 5
print("Factorial of", num, "is", factorial(num))
