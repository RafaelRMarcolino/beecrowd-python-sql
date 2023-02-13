#Read an array X[10]. After, replace every null or negative number of X ​by 1.
# Print all numbers stored in the array X.

#Input
#The input contains 10 integer numbers. These numbers ​​can be positive or negative.

#Output
#For each position of the array, print "X [i] = x", where i is the position of 
# the array and x is the number stored in that position.

X = []

for i in range(5):
    
    value = int(input())
    
    if value <= 0: 
        value = 88
        X.insert(i, value)
    
    else:
        X.insert(i, value)    

for i in range(5):
    print('X[{0}] = {1}'.format(i, X[i]))
    
        