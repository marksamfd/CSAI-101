#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

n1 = int(input("enter n1: "))
n2 = int(input("enter n2: "))
sum = 0
avg = 0
domOfAvg = 0
if n1>n2:
    n1,n2= n2,n1

for i in range(n1,n2+1):
    sum = sum +i
    domOfAvg = domOfAvg +1

avg = sum/domOfAvg
print("sum",sum,"avarage",avg)

