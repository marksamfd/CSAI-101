#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 1:23 PM
storeOpen = True
qty = [int(el) for el in input("how many available items in the following departments?\n Meat - Seafood - Milk - Bread - Oil>").split()]
price = [int(el) for el in input("what are the prices of the following?\n Meat - Seafood - Milk - Bread - Oil>").split()]
while storeOpen:
    wanted = [int(el) for el in input("how many do you want of the following?\n Meat - Seafood - Milk - Bread - Oil>").split()]


