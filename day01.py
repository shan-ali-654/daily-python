name = "Ali"
print(f"Day 1 — {name} is shipping daily now.")

quantity = 5
print(f"{quantity}, Type:  {type(quantity)}")

unit_price = 99.50 
print(f"{unit_price}, Type:  {type(unit_price)}")

big_num = 50_000_000
print(f"Number is : {big_num}")

first = "Ali"
last = "Jatt"
full_name = first + " " + last
print(f"Full Name is :{full_name}")
print(f"First 3 letter is :{full_name[0:3]}")

is_paid = True
if  is_paid:
    print("Paid")
else:
    print("Unpaid")


discount_code = None
if discount_code is None:
    print("No Discount")
else:
    print("Discount Added")

unit_price = 99.5095
print(f"UNit Price is : {unit_price:.2f}")

a = 0.1
b = 0.2
c = 0.3
print(a + b == c )

print(True + True)