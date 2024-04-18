ch=int(input("select food category 1:veg,2:non-veg"))
if(ch==1):
    ch=int(input("select your food 1:dosa 2:idly"))
    if(ch==1):
        print("you have ordered dosa..")
    elif(ch==2):
        print("you have ordered idly..")
    else:
        print("invalid choice")
elif(ch==2):
    print("you have selected non-veg dish..")
else:
    print("invalid choice")