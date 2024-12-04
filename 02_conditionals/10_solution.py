pet = "Dog"
pet_age = 5

if pet == "Dog":
    if pet_age < 2:
        pet_food = "Puppy food"
    else:
        pet_food = "Senior dog food"
else:
    if pet_age < 5:
        pet_food = "Cat food"
    else:
        pet_food = "Senior cat food"


print(pet_food)