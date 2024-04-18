import numpy as np

#create an array from list with type float
a1=np.array([[1,2,3],[4,5,6]],dtype='float')#creating an array with all float numbers
print("array contents are:",a1)#displaying the created array

#create array from tuple
a2=np.array((1,2,3))#creating an array from tuples
print("array created from tuple is:",a2)#displaying the created array

#creating a 16*173 array with all zeros
a3=np.zeros((16,173))
print('\nAn array initialized with all zeros:\n',a3)

#creating a 17*17 array with all ones
one=np.ones((17,17))
print('\nAn array initialized with all ones:\n',one)


#create a matrix full of one number
a4=np.full((17,17), -24.6782)#order=17*17,required number=-24.6782
print('\nAn array initialized with all -24.6782:\n',a4)

#create an array with random values
a5=np.random.random((3,2))
print("\nA random array:\n",a5)

#create a sequence of integers from 0 to 40 with steps(interval) of 5
a6=np.arange(0,40,5)#start value is displayed ,end value is not
print("\nA sequential array:",a6)

#create a sequence of 10 values in range 0 to 40
a7=np.linspace(0,40,10)#both stating and ending points is displayed in result
print("\nA sequential array with 10 values between 0 and 40:\n",a7)

#flatten array
all=np.array([[1,2,3],[4,5,6]])
reshaped_array=all.reshape((1,-1))
reshaped_array_2=all.reshape((-1,1))

print("\nOriginal array:\n", all)
print("reshaped array:\n", reshaped_array)
print("reshaped array:\n", reshaped_array_2)

