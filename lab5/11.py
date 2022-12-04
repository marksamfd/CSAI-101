#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

arr1 = input("please enter row of numbers: ").split()
arr2 = input("please enter row of numbers 2: ").split()
sub=[]
for i in range(len(arr1)):
    arr1[i] = int(arr1[i])
for i in range(len(arr2)):
    arr2[i] = int(arr2[i])

if len(arr1) == len(arr2):
    for i in range(len(arr1)):
        sub.append(arr1[i]-arr2[i])
print(sub)
