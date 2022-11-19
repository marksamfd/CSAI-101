x = int(input("please enter a number: "))
for i in range(1,x+1):
    sum = 0 
    for j in range(1,i+1):
        sum = sum+j
    print(sum)