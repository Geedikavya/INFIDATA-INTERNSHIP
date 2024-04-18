a=10
b=0

try:
     div=a/b
     print("res of div:",div)
except ZeroDivisionError as e:
    print("you are trying to divide an integer number by zero")
    print("e value:",e)
print("end")
