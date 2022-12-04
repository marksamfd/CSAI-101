#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:54 PM
N = int(input("please enter N"))
"""for i in range(N):
    print(" " * i, "*", end="")
    print()
for i in range(-N + 1, 1):
    print(" " * abs(i), "*", end="")
    print()"""

for i in range(0,(2*N)):
    if i <= N:
        print(" " * i, end="")
        print("*", end="")
        print()
    else:
        print(" " * abs((2*N)-i), "*", end="")
        print()


