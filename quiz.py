import random
num = random.randint(10,20)
print(num)
for i in range(0,5):
    user = int(input("Guess a number between 10 and 20: "))
    if num == user:
        print("well done")
        break
    else:
        print("Please try again")


