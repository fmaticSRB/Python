##########################################################
# Author: Filip Matic
# Title: ArrayAdd.py
# Description: Program splits array at specified position
# and moves first part to the end
##########################################################

arr = [1,2,3,4,5,6,100,200]
mid = (len(arr) //2 -1)
arr = arr[mid :-1] + arr[0: mid ]
print (arr)
