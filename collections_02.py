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
product_x["price"] = 250
print(product_x)

# Sets

nums = {2, 3, 2, 6, 4, 3, 5}
print(nums) # it prints values but every time those order get changed also remove repeated numbers/items iteself  

nums.add(9)
print(nums)