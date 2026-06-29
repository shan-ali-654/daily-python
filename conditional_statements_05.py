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
