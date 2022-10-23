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


lowestGrade = 0
lowestGradeIndex = 0
highestGrade = 0
highestGradeIndex = 0

counterGrade = 0

for stgrade in validList:
    if int(stgrade) > highestGrade:
        highestGrade = int(stgrade)
        highestGradeIndex = counterGrade
    elif (int(stgrade)<lowestGrade or lowestGrade == 0)and int(stgrade) !=0:
        lowestGrade = int(stgrade)
        lowestGradeIndex = counterGrade
    counterGrade+=1

print("the valid matrix is:",valid, "\nthe valid  is:",validList01,"\nthe avareage  is:",sum/len(validList),"\nthe highest grade is:",highestGrade,
      "\nit's index is:", highestGradeIndex,"\nthe valid lowest grade is:",lowestGrade,"\nit's index is:", lowestGradeIndex,)
#90 10 50 2 -2 1
