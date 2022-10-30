# please note it's same output but same scenerio
for i in range(6):
    weight = int(input("please enter weight: "))
    unit = int(input("\n1 mg\n2 Kg\n3 Ton\nplease enter unit: "))
    if weight < 0:
        print("invalid weight")
        continue
    elif unit <= 0 or unit > 3:
        print("invalid Unit")
        continue
    else:
        if unit == 1:
            print("converting from mg to gram", weight, "mg =", weight / 1000, "gram")
        elif unit == 2:
            print("converting from Kg to gram", weight, "Kg =", weight * 1000, "gram")
        else:
            print("converting from Ton to gram", weight, "Ton =", weight * 10 ** 6, "gram")
