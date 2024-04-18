gender = input("Enter your gender (Male/Female): ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
marital_status = input("Are you married? (Yes/No): ")

if gender == 'female':
    if marital_status == 'married':
        print('Mrs.')
    else:
         print('Ms.')
else:
     print('Mr.')

print("\nHello",first_name,last_name,age," yearsold.")

