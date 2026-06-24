# Lists

fruit_names = ["Apple", "Grapes", "Banana", "Orange"]
print(fruit_names)

print(fruit_names[0])
print(fruit_names[-1])

fruit_names.append("Mango")
print(fruit_names)

fruit_names[1] = "Pineapple"
print(fruit_names)

print(len(fruit_names))

# Tuples

num = (20, 30, 40)
print(num)

num[0] = 23
print(num) # Showing an {TypeError: 'tuple' object does not support item assignment}

person_x = ("Zeeshan", 23 , "N/A")
name, age, job = person_x
print(name)
print(age)
print(job)

# Dicts

product_x = {"name": "Banana", "price":200, "in_Stock": True}
print(product_x)

print(f"Price is {product_x['price']}")

product_x["quantity"] = 25
print(product_x.get("name"))
print(product_x.get("colour"))
print(product_x.get("price"))
product_x["price"] = 250
print(product_x)

# Sets

nums = {2, 3, 2, 6, 4, 3, 5}
print(nums) # it prints values but every time those order get changed also remove repeated numbers/items iteself  

nums.add(9)
print(nums)

num_a = {2, 3, 5, 6}
num_b = {2, 4, 5, 7}

print(f"Union is : {num_a.union(num_b)}")
print(f"Intersection is : {num_a.intersection(num_b)}")
print(f"Difference is : {num_a.difference(num_b)}")
print(f"Difference is : {num_b.difference(num_a)}")

# Casting
num_str = '25'
num_int = int(num_str)
print(f"{num_int} Type : {type(num_int)}")


num_str = '9.99'
num_float = float(num_str)
print(f"{num_float} Type : {type(num_float)}")

num = 100 
num_str = str(num)
print(f"{num_str} Type : {type(num_str)}")


num_float = 9.99
num_int = int(num_float)
print(f"{num_int} Type : {type(num_int)}")  # it round to the first digit 

num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))
print(f"Sum of Both Nums is : {num_1 + num_2}")


greet = "Hello"
print(int(greet)) # it prints following error in terminal :ValueError: invalid literal for int() with base 10: 'Hello'

print(bool(0))
print(bool(""))
print(bool(5))
print(bool('hi'))
# I notice empty or 0 returns False other 2 returns  True