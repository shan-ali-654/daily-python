# Booleans

num, eng = True, False
print(num)
print(eng)

# Assignment
x = 10
x += 5
print(f"Addition : {x}")


x -= 3
print(f"Decerease : {x}")


x *= 2
print(f"Double : {x}")

# Arithmetic
num_1, num_2 = 17, 5
print(f"Sum is : {num_1 + num_2}")
print(f"Difference is : {num_1 - num_2}")
print(f"Product is  : {num_1 * num_2}")

num_1, num_2 = 17, 5
print(f"Dividing is : {num_1/num_2}")
print(f"Whole Number is : {(num_1//num_2)}")

print(f"Modulus is {num_1 % num_2}")

print(2 ** 5)

print(2 + 3 * 4) # it would be 14 ( while i just guessed)

# Comparison

x, y = 7 , 12
if x > y:
    print("X is Bigger")
elif x == y:
    print("It's Equals")
else:
    print("it's not True.")

x, y = 7, 7

num = x == y
print(num)

x = 3 > 5 < 10
print(x)

# Logical
a, b = True, False
if a and b :
    print(True)
else:
    print(False)

if a or b:
    print(True)
else:
    print(False)

age = 20
if age > 18 and age < 30:
    print(f"Your age is {age}. And you are Eligable")
else:
    print(f"Your age is {age}. And you are Not Eligable")

x = True
print(not a)
