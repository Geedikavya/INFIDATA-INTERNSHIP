import numpy as np

four_by_five=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])

#printing first row
s1=four_by_five[0:1,0:6]
print("printing first row:\n",s1)

#printing last row
s2=four_by_five[3:4,0:6]
print("printing last row:\n",s2)

#element printing
s3=four_by_five[2,3]
print("the element is:",s3)

#printing first column
s4=four_by_five[0:4,0:1]
print("printing first column:\n",s4)

#element printing
s5=four_by_five[:,3:]
print("the element is:",s5)

#print last two rows and columns
s6=four_by_five[1:3,3:5]
print("printing last two columns and rows:\n",s6)

