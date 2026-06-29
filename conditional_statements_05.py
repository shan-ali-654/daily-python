# Q1

# build Grade marking 
exam_score = 55
if exam_score >= 90:
    print('Grade is A')
elif exam_score >= 80:
    print("Grade is B")
elif exam_score >= 70:
    print("Grade is C")
elif exam_score >= 60 :
    print("Grade is D")
elif exam_score < 60 :
    print("Grade is F")
else:
    print("Kindly proceed with Number")

# Q2
# Finding leap Year
year = int(input("Enter year in 4 digit format : "))
if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
     print(f"Yes {year} is a leap Year")
else:
     print("No")


# Q3
# Found max number without max function 
num_1, num_2, num_3 = 4, 9, 8
if num_1 > num_2 and num_1 > num_3:
    print(f"Greater Num is '{num_1}' 1st Number.")
elif num_2 > num_3 and num_2 > num_1:
        print(f"Greater Num is '{num_2}' 2nd Number.")
elif num_3 > num_1 and num_3 > num_2:
        print(f"Greater Num is '{num_3}' 3rd Number.")
else:
     print("Wrong Input Kindly proceed with Numbers. ")

# Q4
# Age ticket Validator
person_age = 23
valid_ticket = False

if person_age>= 18 and valid_ticket:
     print("You can gets in.")
elif person_age < 18 and  not valid_ticket:
     print("You are not eligable. Reason both ticket and age.")
elif person_age>= 18 and not valid_ticket:
     print("You not have a Valid ticket that's why you are not eligable.")
elif person_age < 18 and valid_ticket:
     print("Your Age is Low , that's why you are not eligable.")

# Q5
# Today fact Checker
weekend, public_holiday = True, False
if weekend or public_holiday:
     print("Shop is 'Closed'.")
else:
     print("Shop is 'Opened'.") 

# Q6
# ATM Machine proto Type
acc_balance = 5
card_blocked = False
withdrawl_amount = int(input("Enter amount that you want to withdraw :"))

if card_blocked:
    print("Your Card is 'Blocked'. \nWithdrawl is Not Allowed")
elif not card_blocked:
    if withdrawl_amount <= acc_balance:
        print(f"Your Withdrawl amount is : {withdrawl_amount}.")
        acc_balance = acc_balance - withdrawl_amount
        print(f"Remaining Balance is : {acc_balance}")
    elif withdrawl_amount >acc_balance:
        print(f"The balance you entered : {withdrawl_amount},  this is more than your current balance: {acc_balance}")
        print("Insufficient Funds.")
    