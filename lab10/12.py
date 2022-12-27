mat1,mat2 = [],[]
first = int(input("Enter First mat rows"))
sec = int(input("Enter second mat rows"))
print("mat_1=")
for i in range(first):
    mat1.append([int(el) for el in input().split()])
print("mat_2=")
for i in range(first):
    mat2.append([int(el) for el in input().split()])

print(mat1)