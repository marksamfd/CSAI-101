value = int(input("Please enter a number: "))
lists = input("Please enter numbers separated by spaces: ").split()
lessCount = 0
for num in lists:
    if int(num)<= value:
        lessCount += 1
if lessCount == 0:
    print("All items are greater")
else:
    print("there are",lessCount,"values less than or equal",value)
#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

# 10 9 6 20 15
# 10
