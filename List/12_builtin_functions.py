l1=[4,5,6,7,8,10,15,5]
print("l1 is:",l1)

print("length of l1 is:",len(l1))
print("max element in l1 is:",max(l1))
print("min element in l1 is:",min(l1))
print("sum of the l1 is:",sum(l1))
print("element count of 5 is :",l1.count(5))
l1.reverse()
print("reverse of l1:",l1)#the list is updated here

print("element index:",l1.index(15))
l1.clear()
print("using clear():",l1)