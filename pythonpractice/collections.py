Dictionaries
books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaiden's Tale"])
print(books["Margaret Atwood"])

food = {"Potato":["Chips", "Mash"], "Flour":["Chapati","Pasta", "Bread"], "Meat": ["Steak","Burger"]}
print (food["Potato"])
food_name= input("Please enter a food: ")
print((food_name), "can make you the following food:",(", ".join(food[food_name])))

print("before sort")

for x in food.items():
    print(x)

print("after sort")

for k, v in food.items():
    sorted_food ={k:sorted(v)}
    print(sorted_food)