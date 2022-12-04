#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

numbers = input("enter 3 numbers seprated by space").split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(len(numbers)):
    for i2 in range(len(numbers)):
        if numbers[i]<numbers[i2]:
            numbers[i],numbers[i2] = numbers[i2],numbers[i]
print((numbers))
