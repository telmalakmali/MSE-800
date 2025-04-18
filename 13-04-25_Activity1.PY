#1- Activity : Create a NumPy array of the first 10 positive integers. Then:
#Print the array.
#Print the shape and data type of the array.
#Multiply each element by 2 and print the result.

import numpy as np
#to get first 10 possitive integers 
#np.arange(start, stop) generates numbers from start up to (but not including) stop. arrange is a numpy function
first10 = np.arange(1, 11)
print("first 10 integers are",first10)
#print array shape . (.shape tells you the dimensions of a NumPy array. and .shape is also a numpy fuction)
print("Array shape is",first10.shape)
#print array type . (.dtype tells you the dimensions of a NumPy array. and .dtype is also a numpy fuction)
print("Array type is",first10.dtype)
#Multiply each element by 2 and print the result.
print("Array multiplied by 2 will restun:",first10 *2)