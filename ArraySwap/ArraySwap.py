##########################################################
# Author: Filip Matic
# Title: ArraySwap.py
# Description: Program swaps the first and last elements
# of an array
##########################################################

# Swap function 
def swapList(newList): 
    size = len(newList) 
      
    # Swapping  
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp 
      
    return newList 
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
  
print(swapList(newList)) 
