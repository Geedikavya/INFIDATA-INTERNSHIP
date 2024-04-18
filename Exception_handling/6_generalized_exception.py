a=10
b=10
l1=[2,3,4,5]
try:
    print("list element is:",l1[4])
    div=a/b
    print("res of div:",div)
except ZeroDivisionError as e:
    print("you are trying to divide an integer number by zero")
    print("e value:",e)
except Exception as e:#generalised exception
    print("you are at generalised Exception block")
    print("e value:",e)
print("end")

