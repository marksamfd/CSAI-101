x = int(input("please enter a number: "))
sum = 0 
if x % 5 == 0:
    for i in range(1,x+1):
        sum = sum + i
    print(sum)  
