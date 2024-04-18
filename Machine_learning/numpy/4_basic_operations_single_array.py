import numpy as np

a1=np.array([1,2,3,4,5,6])
print(a1)
#add 1 to every element
print("adding 1 to every element:",a1+1)

#subtract 2 to every element
print("subtracting 2 from every element:",a1-2)

#multiply each element by 10
print("multiply each element by 10:",a1*10)

#square each element
print("squaring each element:",a1**2)

#modifying existing array
a1*=2 #a1=a1*2
print("doubled each element of original array:",a1)

#transpose of array
a2= np.array([[1,2,3],[3,4,5],[9,6,0]])

print("\nOriginal array:\n",a2)
print("transpose of array is:\n",a2.T)