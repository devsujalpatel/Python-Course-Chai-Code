banana_color = input("Enter your banana color: ")

if banana_color == "green":
    banana = "unripe"
elif banana_color == "yellow":
    banana = "ripe"
elif banana_color == "brown":
    banana = "overripe"
else:
    banana = "Invalid color" 

print(banana)