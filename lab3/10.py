studentList = input("enter students grades: ").split()
valid = 0
validList01 = []
validList = []
for grade in studentList:
    if int(grade) >=0 and int(grade) <=100:
        valid +=1
        validList01.append(1)
        validList.append(grade)
    else:
        validList01.append(0)
sum = 0
for grade in validList:
    sum+=int(grade)

print(valid, validList01,sum/len(validList))
