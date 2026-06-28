# For Loops

# Q1
# print each city
city_names = ['Lahore', 'Karachi', 'Sialkot', 'Gawadar', ]
for city in city_names:
    print(city)

# Q2
# print each letter
word = 'Normal'
for letter in word:
    print(letter)

# Q3
# print each Key with Value Pairs
person = {
    'name' : 'Shan',
    'age' : 23,
    'City' : 'Lahore'
}
for key, value in person.items():
    print(f"Key is {key} : Value is {value}")

# Range

# Q4
# print num from 1 to 10
for num in range(1, 11):
    print(num)

# Q5
# Print Only Even Num 
for num in range (1, 21):
    if num % 2 == 0 :
        print(f"Even Number is : {num}")

# Position and Pairing 

# Q6
# print each item with index and value
fruits = ["Apple", "Banana", "Lemon", "Orange"]
for index , name in enumerate(fruits):
    print(f"Index is {index}: {name}")

# Q7
# make two differ list print them like paired
names = ['Ali', 'Arslan', 'Shahid', 'Amir']
ages = [23, 24, 32, 25]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# While Loops

# Q8
# printing upto 5
num = 1
while num < 6:
    print(f"Number is {num}.")
    num += 1

# Q9
# askig untill get quit
user_input = input("Enter some Alphabet. :")
while user_input != 'quit':
    print(f"You Enter : {user_input}")
    user_input = input("Enter some Alphabet. :")

# Break and Continue

# Q10
# skipping num 5
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(f"Number is {num}")

# Q11
# stoping at 7
for num in range(1, 11):
    print(num)
    if num == 7:
        break

# List Comprehension

# Q12
#  printing square of each num.
lst = [num ** 2 for num in range(1, 11)]
print(lst)

# Q13
# Making a new list of even num 
eve_num = [num for num in range(1, 11) if num % 2 == 0]
print(eve_num)


# Loops Else (try it )

# Q14
for num in range(1, 6):
    print(num)
else:
    print("It's Done.")

