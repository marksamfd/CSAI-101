dim = int(input("please enter N:"))
mat = []
tracee = 0
for i in range(dim):
    row = input().split()
    if len(row) == dim:
        mat.append(row)
for i in range(len(mat)):
    tracee += int(mat[i][i])
print(tracee)
"""
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""

#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:34 PM
