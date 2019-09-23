##########################################################
# Author: Filip Matic
# Title: ArrayAdd.py
# Description: Program performs and demonstrates
# commands that can be used on lists and array
##########################################################

#Working with lists
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)          	# Prints complete list
print(list[0])       	# Prints first element of the list
print(list[1:3])     	# Prints elements starting from 2nd till 3rd 
print(list[2:])      	# Prints elements starting from 3rd element
print(tinylist * 2) 	# Prints list two times
print(list + tinylist) 	# Prints concatenated lists

#Working with types
i = 42   # data type is implicitly set to integer
print(i)
i = 42 + 0.11  # data type is changed to float
print(i)
i = "forty"  # and now it will be a string 
print(i)

# To define an integer use:
myint = 7
# To define a floating point number, use:
myfloat = 7.0
myfloat = float(7)

# To define a string use:
mystring = 'hello'
mystring = "hello"


#We can perform simple operations on numbers and strings
one = 1
two = 2
three = one + two
print(three)

# Assignments can be done simultaneously on the same line
a, b = 3, 4


# Tuples:
# A tuple is another sequence data type that is similar to the list. 
# A tuple consists of a number of values separated by commas. 
# Unlike lists, however, tuples are enclosed within parentheses.

tuple = ( 'abcd', 786 , 2.23, 'john'  )

print(tuple)           # Prints complete list
print(tuple[0])        # Prints first element of the list
print(tuple[1:3])     # Prints elements starting from 2nd till 3rd 
print(tuple[2:])       # Prints elements starting from 3rd element



# We can perform certain operations on lists:

List_Test = [1, 2, 3]
List_Test_2 = [4, 5, 6]

# Find length of list
x = len(List_Test)
print(x)
x = len([1, 2, 3])
print(x)

# Concatinate lists
List_new = List_Test + List_Test_2
print(List_new)
List_new_2 = [1, 2, 3] + [4, 5, 6]
print(List_new_2)


# Repeat lists
List = ["hi"]
List_new = List * 4
print(List_new)

# We can check the membership of an element in a list
List = [1, 2, 3]
if 3 in List:
	print("True")

# We can print the list if we need to:
for x in [1, 2, 3]:
	print(x)

# We can update our lists as we go along
list = ['physics', 'chemistry', 1997, 2000];
print("Value available at index 2 : ")
print(list[2])
list[2] = 2001;
print("New value available at index 2 : ")
print(list[2])

# We can delete list items as needed
list = ['physics', 'chemistry', 1997, 2000];
print(list[1])
del list[2]
print("After deleting value at index 2")
print(list)

# Other list operations:
cmp(list1, list2) 	#Compares elements of both lists.
len(list) 			#Gives the total length of the list.
max(list) 			#Returns item from the list with max value.
min(list)			#Returns item from the list with min value.
list(seq)			#Converts a tuple into list.



