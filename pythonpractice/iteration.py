count = 0
name = str(input("What is your name?"))

while count < 5:
    print(name, "is awesome!")
    count += 1

# We will write a for loop which prints all the numbers between 5 and 10.

for i in range(5, 11):
    print(i)

# Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"

name_list = []
max_length = 5

while len(name_list) < max_length:
    names = input("Enter your name: ")
    name_list.append(names)
    print(name_list)
    
for i in name_list:
    print(i, "is awesome!")


# # Work out what the following for loop does:

for i in range(10, 21, 2):
    print(i)
Run the code to check.