arr1 = input("please enter an array:").split()
arr2 = input("please enter another array:").split()
dup = []

for i in range(len(arr1)):
    arr1[i] = int(arr1[i])
for i in range(len(arr2)):
    arr2[i] = int(arr2[i])

for el in arr1:
    c = 0
    for el2 in arr2:
        if el == el2:
            c+=1
    dup.append(c)

print(dup)

#1 8 7 5
#5 3 1 7 6 7 7