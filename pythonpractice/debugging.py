# #Exercise1 
user_funds = 10.31
price = {"Burger": 10}
item_price = price=["Burger"]

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print("Sorry you don't have enough money")

# #Exercise2
def product(n):
    total = 1
    for i in n:
        total *= i
    return total

print(product([4,4,5]))

# #Exercise3

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(15))
print(is_prime(20))

# #Exercise4 

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print (i)
    n = n+1 

print (item_list[4])
