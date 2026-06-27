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
