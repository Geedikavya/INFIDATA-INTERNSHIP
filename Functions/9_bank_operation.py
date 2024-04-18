def create_account():
    global name,mobile,branch,balance
    name=input("enter your name:")
    mobile=input("enter your mobile number:")
    branch=input("enter your branch:")
    balance=float(input("enter your initial balance:"))
def deposit():
    global balance
    dep=float(input("enter an amount to deposit:"))
    balance=balance+dep
    print("updated balance after deposite:",balance)
def withdraw():
    global balance
    wd=float(input("enter an amount to withdraw:"))
    if(balance>=wd):
        balance=balance-wd
        print("updated balance after withdraw:",balance)
    else:
        print("insuffient balance")
def display():
    print("customer name:",name)
    print("customer mobile number:",mobile)
    print("customer branch:",branch)
    print("available balance:",balance)

print("welcome to SBI bank,create your account")
create_account()
while(True):
    ch=int(input("enter your choice 1:deposit 2:withdraw 3:display 4:exit"))
    if (ch == 1):
        deposit()
    elif (ch == 2):
        withdraw()
    elif (ch == 3):
        display()
    elif (ch == 4):
        exit(0)
    else:
        print("invalid choice")