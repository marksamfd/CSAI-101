arr1 = input("please input array").split()
arr2 = input("please input array 2").split()
exist = True
for i in range(len(arr1)):
    arr1[i] = int(arr1[i])
for i in range(len(arr1)):
    arr2[i] = int(arr2[i])

for el in arr1:
    for el2 in arr2:
        if el == el2:
            print("Duplicate found")
            exit()
print("no duplicate found")

#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

# 1 8 7 5
# 5 3 1 7 6 7 7
# 3 3 2 9 6
