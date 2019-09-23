##########################################################
# Author: Filip Matic
# Title: PythonOperations.py
# Description: Program creates and executes multiple
# different, basic, python operations
##########################################################

def Lists():
	list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
	tinylist = [123, 'john']

	print(list)          	# Prints complete list
	print(list[0])       	# Prints first element of the list
	print(list[1:3])     	# Prints elements starting from 2nd till 3rd 
	print(list[2:])      	# Prints elements starting from 3rd element
	print(tinylist * 2) 	# Prints list two times
	print(list + tinylist) 	# Prints concatenated lists

	# We can also print the individual elements in the list
	for x in list:
		print(x)

def Tuples():
	# Tuples:
	# A tuple is another sequence data type that is similar to the list. 
	# A tuple consists of a number of values separated by commas. 
	# Unlike lists, however, tuples are enclosed within parentheses.
	
	tuple = ( 'abcd', 786 , 2.23, 'john'  )
	
	print(tuple)           # Prints complete list
	print(tuple[0])        # Prints first element of the list
	print(tuple[1:3])     # Prints elements starting from 2nd till 3rd 
	print(tuple[2:])       # Prints elements starting from 3rd element

def Type():
	i = 42   # data type is implicitly set to integer
	print(i)
	i = 42 + 0.11  # data type is changed to float
	print(i)
	i = "forty"  # and now it will be a string 
	print(i)

def IntegerDef():
	# To define an integer use:
	myint = 7
	print(myint)
	# To define a floating point number, use:
	myfloat = 7.0
	print(myfloat)
	myfloat = float(7)
	print(myfloat)

def Strings():
	# To define a string use:
	mystring = 'hello'
	print(mystring)
	mystring = "hello"
	print(mystring)

def String_Int_Ops():
	#We can perform simple operations on numbers and strings
	one = 1
	two = 2
	three = one + two
	print(three)

def ListLength():
	list = [1, 2, 3]

	#We can find the length of a list in 2 ways:
	x = len(list)
	print(x)
	x = len([1, 2, 3])
	print(x)

def listMaxMin():
	# We can find the max and min values of a list
	list = [1, 2, 3, 4, 5, 6]
	x = max(list)
	y = min(list)
	print(x)
	print(y)

def ListConcat():
	# We can concatinate lists together
	list_2
	List_new = list + list_2
	print(List_new)
	List_new_2 = [1, 2, 3] + [4, 5, 6]
	print(List_new_2)

def ListRepeat():	
	# We can repeat the values of a list
	list = ["hi"]
	list_new = List * 4
	print(List_new)

def ListMembership():
	# We can check if a value is contained within a list
	list = [1, 2, 3]
	if 3 in list:
		print("true")

def ListEdits():
	# We can make changes to out list if we need to

	# We can change the value of an element in the list
	list = ['physics', 'chemistry', 1997, 2000];
	print("Value available at index 2 : ")
	print(list[2])
	list[2] = 2001;
	print("New value available at index 2 : ")
	print(list[2])

	# We can also delete elements as needed
	list = ['physics', 'chemistry', 1997, 2000];
	print(list[1])
	del list[2]
	print("After deleting value at index 2")
	print(list)

def List2Tuple():
	# We can convert a list into a tuple
	list = [1, 2, 3, 4, 5, 6]
	list(seq)

def ListCompare():
	# We can compare the values in two lists
	list = [1, 2, 3]
	list2 = [1, 2, 3]
	cmp(list, list2)
	if cmp(list, list2) == 0:
		print("Lists are the same")


""" Compare Function Note:
	
	The built-in cmp() function is no longer available since the 
	release of Python 3.0. As a result we have built our own

	In reality, the use of the cmp() function is not too common. 
	If you are needing this function, you might want to examine
	if it's really the best method for what you need

"""

def cmp(a, b):
    return (a > b) - (a < b) 

    # Function will return 0 if values are equal, 1 if a > b, and -1 if b > a

def ArithOps():
	# Python follows the Order of operations and can be used as such:
	number = 1 + 2 * 3 / 4.0
	print(number)

	# We can use the modulo operator, which returns the integer remainder of the division
	remainder = 11 % 3
	print(remainder)

	# We can use 2 multiplication symbols to make a power relationshio
	squared = 7 ** 2
	cubed = 2 ** 3
	print(squared)
	print(cubed)

def StringOps():
	# Python supports concatinating strings using the add operator
	helloworld = "hello" + " " + "world"
	print(helloworld)
	stringrepeat = "hello" * 3
	print(stringrepeat)

	# We can use the index command. The command will print the location of the first occurance of the letter
	# or phrase we list. If there are more than one occurance, python will ignore it and only print the first
	astring = "hello World"
	print(astring.index("o"))

	# We can print our string in eithe upper or lower case
	print(astring.upper())
	print(astring.lower())

def Conditions():
	# Python uses boolean variables to evaluate conditions. The values True and False are returned when an 
	# expression is compared or evaluated
	x = 2
	print(x==2)		# Prints out true
	print(x==3)		# Prints out False
	print(x<3)		# Prints out true

def BooleaonOps():
	name = "John"
	age = 23
	if name == "John" and age == 23:
		print("Your name is John, and you are also 23 years old.")
	
	if name == "John" or name == "Rick":
		print("Your name is either John or Rick.") 

