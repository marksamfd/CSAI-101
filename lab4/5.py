soup = "vegetables(v), seafood, mushroom(v), chicken".split(",")
meal = "burger, grilled chicken, mashed potatoes(v), veggie burger(v)".split(",")
userSoup = input("enter your favourite soup")
soupVeg = False
userMeal = input("enter your favourite meal")
mealVeg = False
for i in range(len(soup)):
    if userSoup in soup[i] and "(v)" in soup[i]:
        soupVeg = True
for i in range(len(meal)):
    if userMeal in meal[i] and "(v)" in meal[i]:
        mealVeg = True

if soupVeg and mealVeg:
    print("She loves vegetables")
else:
    print("She hates Vegetables")

