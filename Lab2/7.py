#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

x = int(input("enter a number:"))
if x>=0:
    add = 0
    for i in range(1,x+1):
        add = add + i
    print(add)
else:
    print("number should be positive")
