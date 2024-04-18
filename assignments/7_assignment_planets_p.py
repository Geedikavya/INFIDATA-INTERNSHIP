earth_weight = float(input("Enter your Earth weight: "))
planet_gravity = ("1.venus \n 2.mars\n 3.jupiter\n 4.saturn\n 5.uranus\n 6.neptune")
print("I have information for the following planets:\n",planet_gravity)
ch=int(input("which planet are you visting?"))
if (planet_gravity == 1):
    planetweight = earth_weight * 0.78;
    print("weight in venus planet is:", planetweight)
elif (planet_gravity == 2):
    planetweight = earth_weight * 0.39;
    print("weight in mars planet is:", planetweight)
elif (planet_gravity == 3):
    planetweight = earth_weight * 2.65;
    print("weight in jupiter planet is:", planetweight)
elif (planet_gravity == 4):
    planetweight = earth_weight * 1.17;
    print("weight in saturn planet is:", planetweight)
elif (planet_gravity == 5):
    planetweight = earth_weight * 1.05;
    print("weight in uranus planet is:", planetweight)
elif (planet_gravity == 6):
    planetweight = earth_weight * 1.23;
    print("weight in neptune planet is:", planetweight)







