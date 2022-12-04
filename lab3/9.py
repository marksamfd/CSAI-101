#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

s1 = input("enter string: ")
s2 = input("enter string: ")
mismatch = []
for i in range(len(s1)):
    if s2[i] != s1[i]:
        mismatch.append(i)

if len(mismatch) > 0:
    for i in mismatch:
        print("mismatch at index:",i)
else:
    print("identical String")
