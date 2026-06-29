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
    