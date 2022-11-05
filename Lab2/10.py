sumO = 0
sumE = 0

for i in range(1,6):
    x = int(input("enter x: "))
    if x%2 == 0:
        sumE = sumE + x
    else:
        sumO = sumO+ x
print("sum of even",sumE,"sum of odd",sumO)
