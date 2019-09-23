##########################################################
# Author: Filip Matic
# Title: compound_interest.py
# Description: This code caluclates the interest given by"
# Compound Interest = P(1 + R/100)
# Where:
# P = Principle Amount, T = Time, R = Rate
##########################################################

P = 100000
T = 5
R = 3

#Calculate the Compound Interest
CI = P * (1 + (R/100))

#Print the value
print("The Compound Interest is", CI)
