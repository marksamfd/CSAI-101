#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 11:27 AM

l = input("please enter a list").split()
n = int(input("please enter a number"))
c = 0
for i in range(len(l)):
    l[i] = int(l[i])

l.sort()
print(l)
"""for i in range(len(l)):
    for k in range(i+1, len(l)):
        if l[i]+l[k] == n:
            c += 1
print(c)
"""
