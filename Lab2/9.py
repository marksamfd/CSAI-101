sum = 0
avg = 0
domOfAvg = 0
for i in range(1,6):
    x = int(input("enter n1: "))
    if x>6:
        sum = sum + x
        domOfAvg = domOfAvg+1
avg = sum/domOfAvg
print("sum",sum,"avarage",avg)

