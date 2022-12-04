#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:45 PM

grades1 = input("enter 3 numbers seprated by space").split()
names1 = input("please enter students names").split()

for i in range(len(grades1)):
    grades1[i] = int(grades1[i])

for i in range(len(grades1)):
    for i2 in range(len(grades1)):
        if grades1[i]>grades1[i2]:
            grades1[i],grades1[i2] = grades1[i2],grades1[i]
            names1[i],names1[i2]=names1[i2],names1[i]
print(grades1,names1)
