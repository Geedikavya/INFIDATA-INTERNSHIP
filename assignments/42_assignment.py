def distance():
    km=int(input("enter the no.of kilometers:"))
    if (km <= 10):
        charge=80
        print("charge is:",charge)
    elif (km >=11 and km <= 20):
        charge=km*6+80
        print("charge is:",charge)
    elif (km >=21 and km<= 30):
        charge=km*5+80
        print("charge is:",charge)
    else:
        charge=km*4+80
        print("charge is:",charge)
distance()